from odoo import api, models, fields
import string
# from random import sample, choice
import random
from odoo.exceptions import ValidationError
import re
import secrets
import string
 # table defination
    # '''
    # _rec_name,  
    # _date_name, 
    # _fold_name, 
    # _parent_store, 
    # _parent_name, 
    # _check_company_auto, 
    # _description, 
    # _sql_constraints, 
    # _sequence,
    # _table, 
    # _log_access 
    # _auto, 
    # _translates
    # ''' 
class StudentData(models.Model):
    _name = 'student.data'
    _description = 'Student Data'
    _rec_name = 'username'
    _order = 'id'


    GENDER = [
        ('m','Male'),
        ('f','Female'),

    ]


    # # @api.depends('password')
  

    full_name = fields.Char()
    username = fields.Char(required=True, string='Username')
    gender = fields.Selection(GENDER, default='m')
    address = fields.Text(required=True, )
    bio = fields.Text() 
    phone_number = fields.Char(required=True, )
    date_of_birth = fields.Date()
    image = fields.Binary()
    student_code = fields.Char(string='Code', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    email = fields.Char(required=True, )
    password = fields.Char(readonly=True, compute='_generate_password',store=True,)
    # final = fields.Char()
    postal_code  = fields.Integer(required=True, )
    pass_depend = fields.Char()

    @api.depends('pass_depend')
    def _generate_password(self):
        for rec in self:
            # if rec.pass_depend != None:
            letters = (string.punctuation + string.digits + string.ascii_letters)
            result = ''.join(random.choice(str(letters)) for i in range(10))
                # print(result)
            rec.password = result



    _sql_constraints = [
        ('username', 'unique(username)', 'Please Enter Unique Username'),
    ]

    @api.constrains('phone_number')
    def validate_phone(self):
        for i in self:
            if re.match(r'^(?:\+?44)?[07]\d{9,13}$', i.phone_number) == None:
                raise ValidationError("Please Provide Valid Phone Number: %s" % i.phone_number)
        return True
    

    @api.constrains('email')
    def validate_email(self):
        for obj in self:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", obj.email) == None:
                raise ValidationError("Please Provide Valid Email Address: %s" % obj.email)
        return True
    
  
  
    # @api.constrains('postal_code')
    # def validate_postal_code(self):
    #     for j in self:
    #         if re.match("^\\d{5}$", j.postal_code) == None:
    #             raise ValidationError("Please Provide valid Postal Code: %s" % j.postal_code)
    #         return True




    @api.model
    def create(self, vals):
        if vals.get('student_code', _('New')) == _('New'):
            vals['student_code'] = self.env['ir.sequence'].next_by_code('student.data.sequence') or _('New')
        return super(StudentData, self).create(vals)
    
    # @api.model
    # def write(self, *values):
    #     return super(StudentData, self).write(values)