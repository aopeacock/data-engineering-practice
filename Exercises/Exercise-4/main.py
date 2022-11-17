import glob
import json
import csv


def get_file_names():
    arr = []
    for filename in glob.iglob('./data/**/*.json', recursive=True):
        arr.append(filename)
    return arr


def flatten_data(inp):
    res = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            res[name[:-1]] = x
    flatten(inp)
    return res


def main():
    file_list = get_file_names()
    for file in file_list:

        with open(file) as json_file:
            jsondata = json.load(json_file)
        flat_json = flatten_data(jsondata)
        if file.find('/'):
            filename = file.rsplit('/', 1)
            file_name = filename[1].rsplit('.', 1)
        data_file = open(f'./csv_data/{file_name[0]}.csv', 'w', newline='')
        csv_writer = csv.writer(data_file)

        header = flat_json.keys()
        csv_writer.writerow(header)
        csv_writer.writerow(flat_json.values())
        data_file.close()


if __name__ == '__main__':
    main()
