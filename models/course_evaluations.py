from odoo import models, fields

class Evaluations(models.Model):
    _name = 'course.evaluations'
    _description = 'Course Evaluations'

    evaluation_description = fields.Text(string='Evaluation Description')
    evaluation_date = fields.Date(string='Evaluation Date')
    evaluation_weighting = fields.Float(string='Evaluation Score')
    course_id = fields.Many2one('grades.course', string='Course')

