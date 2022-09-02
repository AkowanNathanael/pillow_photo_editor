from flask_wtf import FlaskForm,Form,RecaptchaField
from wtforms import StringField,IntegerField,SubmitField,FileField
from wtforms.validators import InputRequired, Length


class Fileform(FlaskForm):
    file=FileField("Upload File",validators=[InputRequired("You must enter a file")])
    upload_image=StringField("Upload Image",validators=[InputRequired("")])
    width=IntegerField("width",validators=[InputRequired("Enter a number"),Length(max=1980,min=60,message="file width must be between 50 and 1980")])
    height=IntegerField("height",validators=[InputRequired("Enter a number"),Length(max=1980,min=60,message="file height must be between 50 and 1980")])
    recapture=RecaptchaField()
    submit=SubmitField("resize")