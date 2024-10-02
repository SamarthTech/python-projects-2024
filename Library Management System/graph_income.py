import matplotlib.pyplot as plt

import calendar


class Graph:
    def __init__(self, con):
        self.cursor=con.cursor()
        self.generate_income_analysis()

    def generate_income_analysis(self):


        months = list(calendar.month_name)[1:]

        v = "select count(*), Month(regdate) from Userdetails group by Month(regdate);"
        self.cursor.execute(v)
        r = self.cursor.fetchall()

        d = {"January": 0, "February": 0, "March": 0, "April": 0, "May": 0, "June": 0, "July": 0, "August": 0,
             "September": 0, "October": 0, "November": 0, "December": 0}

        for i in r:
            monthname = months[i[1] - 1]
            d[monthname] = i[0]

        L=[]
        for i in d.values():
            L.append((i*500))

        plt.figure(figsize=(12, 4))
        plt.plot(months, L)

        plt.xlabel('Months')
        plt.ylabel('Income')
        plt.title('Income from Registration')

        plt.show()


# Example usage:
# graph = Graph(host="localhost", user="root", passwd="Sayantan@123", database="Library")
# graph.generate_income_analysis()


