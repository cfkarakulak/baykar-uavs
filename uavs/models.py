from django.db import models


class Uav(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        "auth.User", related_name="creator", on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        "UavCompany", related_name="company", on_delete=models.SET_NULL, null=True
    )
    brand = models.ForeignKey(
        "UavBrand", related_name="brand", on_delete=models.SET_NULL, null=True
    )
    category = models.ForeignKey(
        "UavCategory", related_name="category", on_delete=models.SET_NULL, null=True
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name


class UavCompany(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UavBrand(models.Model):
    company = models.ForeignKey(
        "UavCompany",
        related_name="uav_brand_company",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UavCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
