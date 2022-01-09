import csv

def save_to_file(datas):
    with open("datas_by_flask.csv",mode="w",newline='',encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(["title", "data sorce", "info", "details link"])
        for data in datas:
            writer.writerow(list(data.values()))
    return