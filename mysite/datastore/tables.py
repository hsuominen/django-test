import django_tables2 as tables
from datastore.models import acquisition, coordinate, value


class AcquisitionTable(tables.Table):

    coordinate_label_1 = tables.Column(empty_values=())
    coordinate_label_2 = tables.Column(empty_values=())

    def render_coordinate_label_1(self, record):
        # Concatenates all coordinate_labels into a string
        return record.coordinates.all()[0].coordinate_label

    def render_coordinate_label_2(self, record):
        # Concatenates all coordinate_labels into a string
        return record.coordinates.all()[1].coordinate_label

    #coordinate_label = tables.Column(empty_values=())

    # def render_coordinate_label(self, record):
    #     # Concatenates all coordinate_labels into a string
    #     return ', '.join([coords.coordinate_label for coords in record.coordinates.all()])

        # See http://django-tables2.readthedocs.org/en/latest/#
        # Table.render_FOO() methods
        # To change how a column is rendered, implement a render_FOO method on
        # the table (where FOO is the column name). This approach is suitable
        # if you have a one off change that you don't want to use in multiple
        # tables.

        # Supported keyword arguments include:

        # record - the entire record for the row from the table data
        # value - the value for the cell retrieved from the table data
        # column - the Column object
        # bound_column - the BoundColumn object
        # bound_row - the BoundRow object
        # table - alias for self

    # This also works - but does not use the record explicitly
    # def render_coordinate_label(self):

    #     for i in acquisition.objects.all():
    #         return i.coordinates.all()[1]

        # for j in i.coordinates.all():
        #   print j
        #     print i.coordinates.all()[1]
        #   return j.coordinate_label

    class Meta:
        model = acquisition
        attrs = {"class": "paleblue"}
        fields = (
            'acqdatetime', 'coordinate_label_1','coordinate_label_2')
        sequence = (
            'acqdatetime', 'coordinate_label_1','coordinate_label_2')
