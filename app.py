#################### Python APP ####################
####################  XFOTOS APP ####################
from flask import Flask;from flask import request,render_template,send_file,flash
from PIL import Image;import os
# from flask_uploads import UploadNotAllowed,UploadSet,IMAGES,configure_uploads
from werkzeug.utils import secure_filename;from forms import Fileform



# App xfotos
app=Flask(__name__)
# images=UploadSet("photos",IMAGES)

app.config.from_pyfile("config.cfg")
# configure_uploads(app,images)



# Home page route
@app.route("/",methods=["GET","POST"])
@app.route("/home",methods=["GET","POST"])
def index():
    form=Fileform()
    if request.method=="POST":
        im=request.files["file"]
        # im.read()
        # file_image=images.save(request.files["file"])
        file_width=int(request.form["width"])
        file_height=int(request.form["height"])
        size=(file_width,file_height)
        filename=secure_filename(im.filename)
        image=Image.open(im)
        
        image=image.resize(size,Image.BICUBIC)
        image.save("static"+ "\\uploads\\"+filename)
        flash("Image successfully processed, check your download folder for image")
        # return send_file(BytesIO(im.read()),mimetype="Image",as_attachment=True,download_name="hio.PNG")
        return send_file("static"+"\\uploads\\" +filename,mimetype="image",attachment_filename=filename,as_attachment=True);os.remove("static/"+"uploads"+filename)
        
        
    return render_template("home.html",form=form)





# error handler page not found
@app.errorhandler(404)
def page_not_found(e):
    return  render_template("404.html")



# error handler internal server error
@app.errorhandler(500)
def internal_server_error(e):
    return  render_template("500.html")


# About route
@app.route("/about",methods=["GET","POST"])
def about():
    form=Fileform()
    if request.method=="POST":
        pass
    return render_template("about.html",form=form)




# convert black and white route
@app.route("/convert_to_bw",methods=["GET","POST"])
def convert():
    form=Fileform()
    if request.method=="POST":
        im=request.files["file"]
        # im.read()
        # file_image=images.save(request.files["file"])
        filename=secure_filename(im.filename)
        image=Image.open(im)
        image=image.convert("L")
        image.save("static"+ "\\uploads\\"+filename)
        flash("Image successfully processed, check your download folder for image")
        # return send_file(BytesIO(im.read()),mimetype="Image",as_attachment=True,download_name="hio.PNG")
        return send_file("static"+"\\uploads\\" +filename,mimetype="image",attachment_filename=filename,as_attachment=True);os.remove("static/"+"uploads"+filename)
    return render_template("convert.html",form=form)



# thumbnail route
@app.route("/thumbnail",methods=["GET","POST"])
def thumbnail():
    form=Fileform()
    if request.method=="POST":
        im=request.files["file"]
        # im.read()
        # file_image=images.save(request.files["file"])
        filename=secure_filename(im.filename)
        image=Image.open(im)
        file_width=int(request.form["width"])
        file_height=int(request.form["height"])
        size=(file_width,file_height)
        image.thumbnail(size=size,resample=3)
        image.save("static"+ "\\uploads\\"+filename)
        flash("Image successfully processed, check your download folder for image")
        # return send_file(BytesIO(im.read()),mimetype="Image",as_attachment=True,download_name="hio.PNG")
        return send_file("static"+"\\uploads\\" +filename,mimetype="image",attachment_filename=filename,as_attachment=True);os.remove("static/"+"uploads"+filename)
    return render_template("thumbnail.html",form=form)


# password generator route
@app.route("/password_generator",methods=["GET","POST"])
def password_generator():
    form=Fileform()
    if request.method=="POST":
        pass
    return render_template("password_generator.html",form=form)


# Xconvert route
@app.route("/xconvert",methods=["GET","POST"])
def xconvert():
    form=Fileform()
    if request.method=="POST":
        im=request.files["file"]
        filename=secure_filename(im.filename)
        image=Image.open(im)
        image=image.convert("RGB")
        file_extension=(request.form["extension"])
        image.save("static"+ "\\uploads\\"+filename+file_extension)
        flash("Image successfully processed, check your download folder for image")
        # return send_file(BytesIO(im.read()),mimetype="Image",as_attachment=True,download_name="hio.PNG")
        return send_file("static"+"\\uploads\\" +filename+file_extension,mimetype="image",attachment_filename=filename+file_extension,as_attachment=True);os.remove("static/"+"uploads"+filename)
    return render_template("xconvert.html",form=form)





if __name__=="__main__":
    app.run()


