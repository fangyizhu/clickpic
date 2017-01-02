import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import validate_comma_separated_integer_list


class Puzzle(models.Model):
    # meta
    id = models.SlugField(primary_key=True, unique=True, editable=False, max_length=6)
    creation_date = models.DateTimeField(default=timezone.now)
    creator = models.CharField(max_length=50)
    creator_email = models.EmailField()

    # puzzle
    row = models.IntegerField()
    column = models.IntegerField()
    x = models.CharField(max_length=500)
    y = models.CharField(max_length=500)

    # solution
    solution = models.CharField(validators=[validate_comma_separated_integer_list], max_length=500)
    image_url = models.URLField()

    def as_json(self):
        return dict(
            id=self.id,
            dimensions=[self.row, self.column],
            solution=map(int, self.solution.split(',')),
            data=dict(x=self.x, y=self.y),
            image=self.image_url
        )

    def __str__(self):
        return '{} {} {}'.format(self.id, self.creator, self.creation_date)

    def created_this_year(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(years=1)

# p = Puzzle(id="123abc", creation_date=timezone.now(), creator="fangyi", creator_email="fangyizhu416@gmail.com", row=5, column=5, x="[[1],[1],[4],[3],[3,1]]", y="[[1,1],[1,1],[4],[2],[3]]", solution="[1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1]", image_url= "https://danbooru.donmai.us/data/__kawashiro_nitori_touhou_drawn_by_ica__20b9c2dd44a2e5d1fff8328441aac750.jpg")
