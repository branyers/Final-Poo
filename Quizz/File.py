import csv


class File:

    def __init__(self, path, name, files, extension):
        self.path = path
        self.name = name
        self.files = files
        self.headers = ["Rank", "First Name", "Last Name", "Attempt #", "Accuracy", "Score"]
        self.extension = extension
        self.flag = False

    def join_csv(self):
        try:
            for index, file in enumerate(self.files):
                data = []
                with open(f"{file}") as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    [data.append({
                        "Rank": row["Rank"],
                        "First Name": row["First Name"],
                        "Last Name": row["Last Name"],
                        "Attempt #": row["Attempt #"],
                        "Accuracy": row["Accuracy"],
                        "Score": row["Score"],
                    })
                        for row in csv_reader]
                    csv_file.close()

                with open(f"{self.name}.csv", "a") as csv_file:
                    csv_writer = csv.DictWriter(csv_file, fieldnames=self.headers)
                    if index == 0:
                        csv_writer.writeheader()
                    csv_writer.writerows(data)
                    csv_file.close()

        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.name}.csv not found")
