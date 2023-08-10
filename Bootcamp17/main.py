from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    with open ('file.txt', 'r', encoding = 'utf -8') as file:
      resultData = list()
      for line in file.readlines():
          resultData.append(tuple(line.split('\n')[0].split(';')))


    # user_name = ['Aleksey', 'Alla', 'Almir', 'Diana', 'Ilali']
    return render_template('base.html', data = resultData)
                            #  title='Главная страница')


# @app.route('/')
# def boot():
#     return render_template('bootcamp.html', title='BootCamp-tasks')
@app.route('/about')
def about():
     return render_template('about.html')


if __name__ == '__main__':
    app.run()
