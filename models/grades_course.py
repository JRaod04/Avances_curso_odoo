from odoo import models, fields


class GradesCourse(models.Model):
    _name = 'grades.course'
    _description = 'Grades Course'
    _order = 'name'

    name = fields.Char(string='Name')
    student_qty = fields.Integer(string='Student Quantity')
    grades_average = fields.Float(string='Grades Average')
    description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Is Activte')
    init_date = fields.Date(string='Initial Date')
    end_date = fields.Date(string='End Date')
    last_evaluation_date = fields.Datetime(string='Last Evaluation Date')
    course_image = fields.Binary(string='Course Image')
    course_shif_selection= fields.Selection([('day','Day'),('nigth','Nigth')])
    teacher_course = fields.Many2one('res.partner', string='Teacher')
    evaluations_course_ids = fields.One2many('course.evaluations','course_id', string='Evaluations')
    state = fields.Selection([("register","Register"), ("in_progress","In Progress"), ("finished","Finished")], string='Status')
