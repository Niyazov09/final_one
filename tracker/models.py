# # from django.db import models
# # from django.contrib.auth.models import User

# # class Project(models.Model):
# #     name = models.CharField(max_length=255)

# #     def __str__(self):
# #         return self.name
    
# # class Task(models.Model):
# #     title = models.CharField(max_length=255)

# #     def __str__(self):
# #         return self.title
# # class Comment(models.Model):
# #     text = models.TextField()

# #     def __str__(self):
# #         return self.text[:30]        


# # class Project(models.Model):
# #     name = models.CharField(max_length=200)
# #     owner = models.ForeignKey(
# #         User,
# #         on_delete=models.CASCADE,
# #         related_name="owned_projects"
# #     )
# #     members = models.ManyToManyField(
# #         User,
# #         related_name="projects",
# #         blank=True
# #     )
# #     created_at = models.DateTimeField(auto_now_add=True)

# #     def is_member(self, user):
# #         return user == self.owner or self.members.filter(pk=user.pk).exists()

# #     def __str__(self):
# #         return self.name

# #     class Meta:
# #         verbose_name = "Project"
# #         verbose_name_plural = "Projects"
# #         ordering = ["-created_at"]


# # class Task(models.Model):
# #     STATUS_CHOICES = [
# #         ("todo", "Todo"),
# #         ("in_progress", "In Progress"),
# #         ("done", "Done"),
# #     ]

# #     PRIORITY_CHOICES = [
# #         ("low", "Low"),
# #         ("medium", "Medium"),
# #         ("high", "High"),
# #     ]

# #     project = models.ForeignKey(
# #         Project,
# #         on_delete=models.CASCADE,
# #         related_name="tasks"
# #     )
# #     title = models.CharField(max_length=200)
# #     description = models.TextField(blank=True)
# #     status = models.CharField(
# #         max_length=20,
# #         choices=STATUS_CHOICES,
# #         default="todo"
# #     )
# #     priority = models.CharField(
# #         max_length=20,
# #         choices=PRIORITY_CHOICES,
# #         default="medium"
# #     )

# #     assignee = models.ForeignKey(
# #         User,
# #         on_delete=models.SET_NULL,
# #         null=True,
# #         blank=True,
# #         related_name="assigned_tasks"
# #     )

# #     created_at = models.DateTimeField(auto_now_add=True)
# #     updated_at = models.DateTimeField(auto_now=True)

# #     def __str__(self):
# #         return self.title

# #     class Meta:
# #         verbose_name = "Task"
# #         verbose_name_plural = "Tasks"
# #         ordering = ["-created_at"]


# # class Comment(models.Model):
# #     task = models.ForeignKey(
# #         Task,
# #         on_delete=models.CASCADE,
# #         related_name="comments"
# #     )
# #     author = models.ForeignKey(
# #         User,
# #         on_delete=models.CASCADE
# #     )
# #     text = models.TextField()
# #     created_at = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return f"Comment by {self.author.username}"

# #     class Meta:
# #         verbose_name = "Comment"
# #         verbose_name_plural = "Comments"
# #         ordering = ["-created_at"]

        



# from django.db import models
# from django.contrib.auth.models import User


# class Project(models.Model):
#     name = models.CharField(max_length=200)
#     owner = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="owned_projects"
#     )
#     members = models.ManyToManyField(
#         User,
#         related_name="projects",
#         blank=True
#     )
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class Task(models.Model):
#     STATUS_CHOICES = [
#         ("todo", "Todo"),
#         ("in_progress", "In Progress"),
#         ("done", "Done"),
#     ]

#     PRIORITY_CHOICES = [
#         ("low", "Low"),
#         ("medium", "Medium"),
#         ("high", "High"),
#     ]

#     project = models.ForeignKey(
#         Project,
#         on_delete=models.CASCADE,
#         related_name="tasks"
#     )
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     status = models.CharField(
#         max_length=20,
#         choices=STATUS_CHOICES,
#         default="todo"
#     )
#     priority = models.CharField(
#         max_length=20,
#         choices=PRIORITY_CHOICES,
#         default="medium"
#     )

#     assignee = models.ForeignKey(
#         User,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name="assigned_tasks"
#     )

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title


# class Comment(models.Model):
#     task = models.ForeignKey(
#         Task,
#         on_delete=models.CASCADE,
#         related_name="comments"
#     )
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Comment by {self.author.username}"


from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owned_projects"
    )
    members = models.ManyToManyField(
        User,
        related_name="projects",
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "Todo"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="todo"
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="medium"
    )

    assignee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tasks"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comment by {self.author.username}"