from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Jar, Transaction

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/dashboard")
@login_required
def dashboard():
    jars = Jar.get_by_owner(current_user.username)
    total_allocated = sum(jar.allocated for jar in jars)
    total_spent = sum(jar.spent for jar in jars)
    return render_template("dashboard/index.html", 
                           jars=jars, 
                           total_allocated=total_allocated, 
                           total_spent=total_spent)

@main.route("/jar/create", methods=["GET", "POST"])
@login_required
def create_jar():
    form = JarForm()
    if form.validate_on_submit():
        name = form.name.data
        allocated = form.allocated.data
        jar = Jar(name, allocated, 0, current_user.username)
        jar.save()
        flash("Jar created successfully!", "success")
        return redirect(url_for("main.dashboard"))

    return render_template("dashboard/create_jar.html", form=form)

@main.route("/transaction/add", methods=["GET", "POST"])
@login_required
def add_transaction():
    jars = Jar.get_by_owner(current_user.username)

    if request.method == "POST":
        jar_name = request.form["jar"]
        amount = float(request.form["amount"])
        description = request.form["description"]
        type = request.form["type"]

        transaction = Transaction(amount, description, type, jar_name, current_user.username)
        transaction.save()

        flash("Transaction added successfully!", "success")
        return redirect(url_for("main.dashboard"))

    return render_template("dashboard/transactions.html", jars=jars)
