from typing import Any

from django import forms
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.utils.translation import gettext_lazy as _

from .forms import CategoryAdminForm, ProductAdminForm
from .models import (
    Category,
    Order,
    OrderProduct,
    Product,
    ProductImage,
    Sale,
    Specification,
    Tag,
)


@admin.action(description='Archive items')
def mark_archived(
    modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet
):
    queryset.update(archived=True)


@admin.action(description='Unarchive items')
def mark_unarchived(
    modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet
):
    queryset.update(archived=False)


class SubcategoryInline(admin.TabularInline):
    model = Category
    verbose_name = _('Subcategory')
    verbose_name_plural = _('Subcategories')


class ParentCategoryListFilter(admin.SimpleListFilter):
    title = _('parent category')
    parameter_name = 'parent__title'

    def lookups(self, request, model_admin):
        queryset = Category.objects.filter(parent=None)
        result = [(category.pk, category.title) for category in queryset]
        return result

    def queryset(
        self, request: Any, queryset: QuerySet[Any]
    ) -> QuerySet[Any] | None:
        if self.value() is None:
            return queryset
        return queryset.filter(parent=self.value())


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    actions = [
        mark_archived,
        mark_unarchived,
    ]
    list_display = ['pk', 'title', 'get_parent_title', 'archived']
    list_display_links = ['pk', 'title']
    search_fields = ['title', 'parent__title']
    list_filter = [ParentCategoryListFilter]
    ordering = ['parent__title', 'title', 'pk']
    sortable_by = []
    form = CategoryAdminForm
    inlines = [SubcategoryInline]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('parent').order_by(
            'parent__title', 'title'
        )

    def get_parent_title(self, obj):
        return obj.parent.title if obj.parent else None

    get_parent_title.short_description = _('Parent')

    def has_delete_permission(self, request, obj=None):
        return False


class ProductImagesInline(admin.TabularInline):
    model = ProductImage
    verbose_name = _('Image')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = [
        mark_archived,
        mark_unarchived,
    ]
    list_display = [
        'pk',
        'title',
        'price',
        'category',
        'count',
        'short_description',
        'free_dlvr',
        'sold',
        'limited',
        'banner',
        'rating',
        'archived',
    ]
    list_display_links = ['pk', 'title']
    ordering = ['title', 'pk']
    search_fields = ['title', 'description', 'full_description', 'price']
    list_filter = ['is_limited_edition', 'is_banner', 'archived']
    form = ProductAdminForm
    readonly_fields = ['created_at', 'sold_count']
    inlines = [ProductImagesInline]
    fieldsets = [
        (
            None,
            {
                'fields': (
                    'title',
                    'category',
                    'price',
                    'count',
                    'sold_count',
                    'free_delivery',
                    'description',
                    'full_description',
                    'created_at',
                ),
            },
        ),
        (
            _('Marketing options'),
            {
                'fields': (
                    'rating',
                    'is_limited_edition',
                    'is_banner',
                ),
            },
        ),
        (
            _('Tags & specifications'),
            {
                'fields': ('tags', 'specifications'),
                'classes': ('collapse',),
            },
        ),
        (
            _('Soft deletion'),
            {
                'fields': ('archived',),
                'classes': ('collapse',),
                'description': _('Field "archived" is for soft delete'),
            },
        ),
    ]

    def short_description(self, obj):
        return obj.description[:20] + '...'

    short_description.short_description = _('Description')

    def limited(self, obj):
        return obj.is_limited_edition

    limited.short_description = _('Limited')

    def banner(self, obj):
        return obj.is_banner

    banner.short_description = _('Banner')

    def sold(self, obj):
        return obj.sold_count

    sold.short_description = _('Sold')

    def free_dlvr(self, obj):
        return obj.free_delivery

    free_dlvr.short_description = _('Free dlvr')

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']


class ProductChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.title} - ${obj.price}"


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = [
        'product',
        'date_from',
        'date_to',
        'sale_price',
    ]
    search_fields = ['product__title', 'date_from', 'date_to', 'sale_price']
    ordering = ['product', 'date_from', 'date_to']
    sortable_by = []

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "product":
            return ProductChoiceField(queryset=Product.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class OrderProductsInline(admin.TabularInline):
    model = OrderProduct
    verbose_name = _('Order product')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    actions = [
        mark_archived,
        mark_unarchived,
    ]
    list_display = [
        'pk',
        'created_at',
        'user',
        'total_cost',
        'full_name',
        'status',
        'delivery_type',
        'archived',
    ]
    list_display_links = ['pk', 'created_at']
    ordering = ['-created_at', 'pk']
    search_fields = [
        'full_name',
        'city',
        'address',
        'email',
        'phone',
        'user__username',
        'total_cost',
        'created_at',
    ]
    list_filter = [
        'status',
        'delivery_type',
        'payment_type',
        'archived',
    ]
    readonly_fields = ['created_at', 'user']
    inlines = [OrderProductsInline]

    def has_delete_permission(self, request, obj=None):
        return False
