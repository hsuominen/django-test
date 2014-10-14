import django_tables2 as tables
from datastore.models import acquisition, coordinate, value


class AcquisitionTable(tables.Table):
    # class Meta:
    #     model = acquisition
    # add class="paleblue" to <table> tag
    #     attrs = {"class": "paleblue"}
    # coordinate_label = tables.Column(empty_values=())

    # def render_coordinate_label(self):
    # 	for a in acquisition:
    # 		b = a.coordinate_label

    #     	return a.coordinate_label

    class Meta:
        model = acquisition

        a = []

        for i in acquisition.objects.all():
            for j in i.coordinates.all():
                a.append(j.coordinate_label)

        #coordinate_label = tables.Column(accessor="coordinates.all()")

    # 	attrs = {"class": "paleblue"}
    # 	fields = ("id","acqdatetime", "coordinate_label")

    clabels = []

    # for k in coordinates:
    #coordinate_label = tables.Column(accessor='coordinates')

    # clabels =
    # tables.Column(accessor='coordinates')#.objects.prefetch_related('coordinates'))

    for i in acquisition.objects.all():
        for j in i.coordinates.all():
            clabels.append(tables.Column(j.coordinate_label))

    print clabels
    aa = clabels[0]

    class Meta:
        model = acquisition
        attrs = {"class": "paleblue"}
        fields = ('acqdatetime','aa')
        sequence = ('acqdatetime', 'aa',)
