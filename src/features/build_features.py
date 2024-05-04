import spacy
from spacy.tokens import DocBin
from spacy.util import filter_spans
import json

class CreateFeatures:

    def __init__(self):
        self.input_path = "./data/interim"
        self.output_path = "./data/processed"

        self.train_data_list = []
        self.dev_data_list = []
        self.test_data_list = []

    def read(self):

        # reading all transformed json files
        self.train_data_list = json.load(open(f"{self.input_path}/NER_TRAIN.json"))
        self.dev_data_list = json.load(open(f"{self.input_path}/NER_DEV.json"))
        self.test_data_list = json.load(open(f"{self.input_path}/NER_TEST.json"))
    
    def create_and_store_feature_sets(self, data_list, name):

        nlp = spacy.blank('en')
        doc_bin = DocBin()

        for record in data_list:
            text = record['text']
            labels = record['entities']
            doc = nlp.make_doc(text)
            ents = []
            for start, end, label in labels:
                span = doc.char_span(start, end, label=label, alignment_mode='contract')
                if not span is None:
                    ents.append(span)
            filtered_ents = filter_spans(ents)
            doc.ents = filtered_ents
            doc_bin.add(doc)

        # writing feature set to processed
        doc_bin.to_disk(f"{self.output_path}/{name}.spacy")


    def execute(self):
        
        # read all the transformed data
        self.read()

        # creates and stores spacy feature sets
        self.create_and_store_feature_sets(data_list=self.train_data_list, name='TRAIN')
        self.create_and_store_feature_sets(data_list=self.dev_data_list, name='DEV')
        self.create_and_store_feature_sets(data_list=self.test_data_list, name='TEST')


def main():
    obj = CreateFeatures()
    obj.execute()

if __name__ == "__main__":
    main()
