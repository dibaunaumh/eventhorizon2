from eventhorizon2.learning.models import Document, Term, Document_Term
from eventhorizon2.learning.nlp import clean_text
import math
from operator import itemgetter
import simplejson

__author__ = 'vlad'

TF_IDF_THRESHOLD = 1.5

def add_document_part(discussion_id, text):

    terms = clean_text(text)
    terms_set = set(terms)
    document = Document.objects.get_or_create(discussion_id = discussion_id)
    number_documents = get_number_documents()

    keywords = {}
    for term in terms_set:
        t = Term.objects.get_or_create(term =term)
        q = Document_Term.objects.filter(document_id = document.id, term_id = t.id)
        if len(q)==0:
            t.num_docs = t.num_docs +1
            t.save()
            dt = Document_Term.objects.create(document_id = document.id, term_id = t.id)
        else:

            dt = q[0]

        dt.tf = float(terms.count(term)) / len(terms)
        dt.save()
        idf = math.log(float(number_documents) / t.num_docs)

        if idf*dt.tf > TF_IDF_THRESHOLD :
            keywords[term] = idf*dt.tf


    sorted_kw = sorted(keywords.items(), key=itemgetter(1), reverse=True)
    old_kw = simplejson.loads(document.keywords)
    for k,v in sorted_kw:
        old_kw[k] =v

    document.keywords = simplejson.dumps(old_kw)
    document.save()



def get_number_documents():
    return Document.objects.all().count()