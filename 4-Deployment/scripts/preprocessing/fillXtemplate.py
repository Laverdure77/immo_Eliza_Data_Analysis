from flask import request

# Fill the X template with values from the form
def fillXtemplate(_X_template):
    # print(request.json['data'])
    _X_template.at[1,'Living area'] = request.json['data'].get('livingArea')
    _X_template.at[1,'Number of rooms'] = request.json['data'].get('rooms')
    _X_template.at[1,'Number of facades'] = request.json['data'].get('facades')
    _X_template.at[1,'Land surface'] = request.json['data'].get('landSurface')
    _X_template.at[1,'Area of garden'] = request.json['data'].get('gardenArea')
    _X_template.at[1,request.json['data'].get('province')] = int('1')
    _X_template.at[1,request.json['data'].get('state')] = int('1')
    _X_template.at[1,request.json['data'].get('subtype')] = int('1')
    # print(_X_template.info())
    return _X_template