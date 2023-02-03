from flask import request

# Fill the X template with values from the form
def fillXtemplate(_X_template):
    _X_template.at[1,'Living area'] = int(request.form['living area'])
    _X_template.at[1,'Number of rooms'] = int(request.form['number of rooms'])
    _X_template.at[1,'Number of facades'] = int(request.form['number of facades'])
    _X_template.at[1,'Land surface'] = int(request.form['land surface'])
    _X_template.at[1,'Area of garden'] = int(request.form['garden area'])
    _X_template.at[1,str(request.form['province'])] = 1
    _X_template.at[1,str(request.form['state'])] = 1
    _X_template.at[1,str(request.form['subtype'])] = 1
    return _X_template