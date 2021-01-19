from flask import Flask,render_template,request, redirect,url_for,flash,session
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'project'

mysql = MySQL(app)
app.secret_key = 'many random bytes'

@app.route('/home')
def Index():
    return render_template('index.html')

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signupuser')
def signupuser():
    return render_template('signupuser.html')

@app.route('/checkuser' ,methods = ['POST'])
def checkuser():
    if request.method == "POST":
        unameuser = request.form['unameuser']
        pswuser = request.form['pswuser']
        cur = mysql.connection.cursor()
        cur.execute(" SELECT * FROM user WHERE Phone_num = %s AND Pasw = %s", (unameuser, pswuser,))
        account = cur.fetchone()
        if account:
           return redirect(url_for('Index'))
        else:
            return redirect(url_for('login'))
    return redirect(url_for('login'))
    
@app.route('/checkastro' ,methods = ['POST'])
def checkastro():
    if request.method == "POST":
        unamepitch = request.form['unamepitch']
        pswpitch = request.form['pswpitch']
        cur = mysql.connection.cursor()
        cur.execute(" SELECT * FROM astropitch WHERE Astro_name = %s AND Pssword = %s", (unamepitch, pswpitch,))
        account = cur.fetchone()
        if account:
           return redirect(url_for('Index'))
        else:
            flash("WRONG INFORMATION HAS ENTERED")
            return redirect(url_for('login'))
    return redirect(url_for('login'))   

@app.route('/signupastro')
def signupastro():
    return render_template('signupastro.html')

@app.route('/user')
def User():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM User")
    data = cur.fetchall()
    cur.close()
    return render_template('user.html', users=data )

@app.route('/userinsert', methods = ['POST'])
def userinsert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        age = request.form['age']
        height = request.form['height']
        weight = request.form['weight']
        location = request.form['location']
        phone_num = request.form['phone_num']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO User (User_name, Age, Height,Weight,Location,Phone_num, Pasw) VALUES (%s, %s, %s, %s, %s ,%s,%s)", (name, age, height,weight,location,phone_num,password))
        mysql.connection.commit()
        return redirect(url_for('login'))

@app.route('/userupdate',methods=['POST','GET'])
def userupdate():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        age = request.form['age']
        height = request.form['height']
        weight = request.form['weight']
        location = request.form['location']
        phone_num = request.form['phone_num']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE User
               SET User_name=%s, Age=%s, Height=%s, Weight=%s, Location=%s, Phone_num=%s
               WHERE User_id=%s
            """, (name, age, height,weight,location,phone_num,id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('User'))


@app.route('/userdelete/<string:id_data>', methods = ['GET'])
def userdelete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM User WHERE User_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('User'))

@app.route('/astro')
def Astro():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM astropitch")
    data = cur.fetchall()
    cur.execute("SELECT astropitch.Astro_name ,count(*) from astropitch, advertisement where advertisement.astro=astropitch.Astro_id group by Astro_name  ORDER by Astro_name ASC")
    firstacc=cur.fetchall()
    cur.execute("SELECT location ,count(*) from astropitch group by location ORDER by location ASC")
    secondacc=cur.fetchall()
    cur.execute("SELECT astropitch.Location ,avg(Price) from astropitch group by location ORDER by price ASC")
    third=cur.fetchall()
    cur.close()
    return render_template('astros.html', astros=data , firstacc=firstacc,secondacc=secondacc, third=third)

@app.route('/astroforprice')
def astroforprice():
    cur = mysql.connection.cursor()
    cur.execute(" SELECT * FROM `astropitch` ORDER BY `astropitch`.`Price` ASC")
    data = cur.fetchall()
    cur.close()
    return render_template('astros.html', astros=data )

@app.route('/astroforpoint')
def astroforpoint():
    cur = mysql.connection.cursor()
    cur.execute(" SELECT * FROM `astropitch` ORDER BY `astropitch`.`Point` DESC")
    data = cur.fetchall()
    cur.close()
    return render_template('astros.html', astros=data )

@app.route('/astroinsert', methods = ['POST'])
def astroinsert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        campaign = request.form['campaign']
        price = request.form['price']
        location = request.form['location']
        point =request.form['point']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO astropitch (Astro_name, Campaign, Price,Location, Point, Pssword) VALUES (%s, %s, %s, %s,%s,%s)", (name, campaign, price,location,point, password))
        mysql.connection.commit()
        return redirect(url_for('login'))

@app.route('/astroupdate',methods=['POST','GET'])
def astroupdate():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        campaign = request.form['campaign']
        price = request.form['price']
        location = request.form['location']
        point = request.form['point']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE astropitch
               SET Astro_name=%s, Campaign=%s, Price=%s, Location=%s , Point= %s
               WHERE Astro_id=%s
            """, (name, campaign, price,location,point,id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Astro'))


@app.route('/astrocalendar/<string:id_data>', methods = ['GET'])
def astrocalendar(id_data):
    cur = mysql.connection.cursor()
    cur.execute("SELECT astropitch.astro_name, calendar.game_day, calendar.game_hour FROM astropitch INNER JOIN calendar ON astropitch.astro_id=%s AND calendar.astro_info=%s",(id_data,id_data))
    data = cur.fetchall()
    cur.close()
    return render_template('astrocalendar.html', astros=data )


@app.route('/astrodelete/<string:id_data>', methods = ['GET'])
def astrodelete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM astropitch WHERE Astro_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Astro'))

@app.route('/adv')
def Adv():
    cur = mysql.connection.cursor()
    cur.execute("SELECT Adv_id, user.User_name, astropitch.Astro_name, Missing_Field, Game FROM user, astropitch, advertisement   WHERE (advertisement.User= user.user_id) AND (advertisement.Astro= astropitch.astro_id)")
    data = cur.fetchall()
    cur.execute("SELECT * FROM Calendar")
    games = cur.fetchall()
    cur.execute("SELECT DISTINCT astropitch.Location, advertisement.Missing_Field FROM astropitch INNER JOIN advertisement ON astropitch.Astro_id= advertisement.Astro")
    acc = cur.fetchall()
    cur.close()
    return render_template('advertisements.html', advs=data,games=games, acc=acc )

@app.route('/calinsert',methods=['POST'])
def calinsert():
     if request.method == "POST":
        flash("Data Inserted Successfully")
        gameday =request.form['gameday']
        gamehour = request.form['gamehour']
        astronum = request.form['astro']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `calendar` (Game_hour, `Game_day`, `Astro_info`) VALUES  (%s, %s ,(SELECT astropitch.Astro_id FROM astropitch where astropitch.Astro_name=%s))", (gamehour,gameday,astronum,))
        mysql.connection.commit()
        return redirect(url_for('Adv'))

@app.route('/advinsert', methods = ['POST'])
def advinsert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        astronum = request.form['astro']
        usernum = request.form['user']
        missing = request.form['missing']
        gamenum = request.form['gamenum']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO advertisement (User, Astro,Missing_Field,Game) VALUES  ( (SELECT user.user_id FROM user where user.user_name=%s ),(SELECT  astropitch.Astro_id FROM astropitch WHERE astropitch.Astro_name=%s) , %s,%s)", (usernum, astronum, missing,gamenum,))
        mysql.connection.commit()
        return redirect(url_for('Adv'))

@app.route('/advupdate',methods=['POST','GET'])
def advupdate():
    if request.method == 'POST':
        id_data = request.form['id']
        usernum = request.form['user']
        astronum = request.form['astro']
        missing = request.form['missing']
        gamenum = request.form['gamenum']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE advertisement
               SET User=%s,Astro=%s,  Missing_Field=%s, Game=%s
               WHERE Adv_id=%s
            """, (usernum, astronum, missing,gamenum,id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Adv'))

@app.route("/advapply", methods = ['GET', 'POST'])
def advapply():
    id_data = request.form['id']
    userid = request.form['user']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO `advertisement_information` (`Adv_info`, `Applicant_info`) SELECT user.user_id, advertisement.Adv_id FROM User,advertisement WHERE user.User_name=%s AND advertisement.Adv_id =%s ", (userid,id_data,))
    mysql.connection.commit()
    flash("Your application has recorded.")
    return redirect(url_for('Adv'))

@app.route('/advdelete/<string:id_data>', methods = ['GET'])
def advdelete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM advertisement WHERE Adv_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Adv'))


@app.route('/campaigns', methods=['GET'])
def campaigns():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM `astropitch` WHERE `Campaign` != 'No campaign'")
    data = cur.fetchall()
    cur.close()
    return render_template('astros.html', astros=data )

@app.route('/kaleci', methods=['GET'])
def kaleci():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  Adv_id, user.User_name, astropitch.Astro_name, Missing_Field, Game  FROM user, astropitch ,advertisement  WHERE (advertisement.User= user.user_id) AND (advertisement.Astro= astropitch.astro_id) AND (`Missing_Field` = 'goalkeeper')")
    data = cur.fetchall()
    cur.close()
    return render_template('advertisements.html', advs=data )


@app.route('/forvet', methods=['GET'])
def forvet():
    cur = mysql.connection.cursor()
    cur.execute("SELECT Adv_id, user.User_name, astropitch.Astro_name, Missing_Field, Game FROM user, astropitch ,advertisement  WHERE (advertisement.User= user.user_id) AND (advertisement.Astro= astropitch.astro_id) AND (`Missing_Field` = 'striker')")
    data = cur.fetchall()
    cur.close()
    return render_template('advertisements.html', advs=data )


@app.route('/defans', methods=['GET'])
def defans():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  Adv_id, user.User_name, astropitch.Astro_name, Missing_Field, Game FROM user, astropitch ,advertisement  WHERE (advertisement.User= user.user_id) AND (advertisement.Astro= astropitch.astro_id) AND (`Missing_Field` = 'defense')")
    data = cur.fetchall()
    cur.close()
    return render_template('advertisements.html', advs=data )

if __name__=="__main__":
    app.run(debug=True)