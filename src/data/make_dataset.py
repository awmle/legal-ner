from glob import glob
import json


class TransformDataset:

    def __init__(self):
        self.input_path = "./data/raw"
        self.output_path = "./data/interim"

        self.train_data_list = []
        self.dev_data_list = []
        self.test_data_list = []

    def read(self):

        # getting paths for all raw json files
        file_paths = glob(f"{self.input_path}/*/*.json")

        # merging all similar data slices to respective dict
        for path in file_paths:
            if "TRAIN" in path:
                self.train_data_list.extend(json.load(open(path)))
            elif "DEV" in path:
                self.dev_data_list.extend(json.load(open(path)))
            elif "TEST" in path:
                self.test_data_list.extend(json.load(open(path)))

    def restructure_data(self):

        # restructuring train data
        temp_list = []
        for record in self.train_data_list:
            temp_dict = {}
            temp_dict["text"] = record["data"]["text"]
            temp_dict["entities"] = [
                (
                    entity["value"]["start"],
                    entity["value"]["end"],
                    entity["value"]["labels"][0],
                )
                for entity in record["annotations"][0]["result"]
            ]
            temp_list.append(temp_dict)
        self.train_data_list = temp_list.copy()

        # restructuring dev data
        temp_list = []
        for record in self.dev_data_list:
            temp_dict = {}
            temp_dict["text"] = record["data"]["text"]
            temp_dict["entities"] = [
                (
                    entity["value"]["start"],
                    entity["value"]["end"],
                    entity["value"]["labels"][0],
                )
                for entity in record["annotations"][0]["result"]
            ]
            temp_list.append(temp_dict)
        self.dev_data_list = temp_list.copy()

        # restructuring test data
        temp_list = []
        for record in self.test_data_list:
            temp_dict = {}
            temp_dict["text"] = record["data"]["text"]
            temp_dict["entities"] = [
                (
                    entity["value"]["start"],
                    entity["value"]["end"],
                    entity["value"]["labels"][0],
                )
                for entity in record["annotations"][0]["result"]
            ]
            temp_list.append(temp_dict)
        self.test_data_list = temp_list.copy()

    def write(self):

        # saving transformed train data to interim
        with open(f"{self.output_path}/NER_TRAIN.json", "w") as f:
            json.dump(self.train_data_list, f, indent=4)

        # saving transformed dev data to interim
        with open(f"{self.output_path}/NER_DEV.json", "w") as f:
            json.dump(self.dev_data_list, f, indent=4)

        # saving transformed test data to interim
        with open(f"{self.output_path}/NER_TEST.json", "w") as f:
            json.dump(self.test_data_list, f, indent=4)

    def execute(self):

        # load all json files
        self.read()

        # change structure for feature engineering
        self.restructure_data()

        # write to interim
        self.write()

def main():
    obj = TransformDataset()
    obj.execute()

if __name__ == "__main__":
    main()
