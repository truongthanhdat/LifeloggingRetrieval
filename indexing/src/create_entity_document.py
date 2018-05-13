import pickle
document = {}

def create_entity():
    print 'Create Entity...'
    csv = open('../../database/Entity.csv', 'r')
    for line in csv:
        array = line.split(',')
        file_name = str(array[0].split('/')[-1])
        print 'Process Entity on %s' % file_name
        if document.has_key(file_name):
            document[file_name] = document[file_name] + " " + str(array[1])
        else:
            document[file_name] = str(array[1])

if __name__ == '__main__':
    create_entity()
    pickle.dump(document, open('../document/entity_document.pickle', 'wb'))
