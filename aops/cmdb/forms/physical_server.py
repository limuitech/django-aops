#coding=utf-8

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _

from libs.forms.common import newModelForm, newChoiceField, EXPIRATION_YEAR_CHOICES
from libs.forms.field import newDateTimeInput, AutoGetVal

class PhysicalServerForm(newModelForm):
    uuid = forms.CharField(max_length=255, label=_('UUID'), widget=AutoGetVal(g_url='cmdb:get_uuid', d_type='cmdb.uuid',attrs={'class':'form-control'}))
    #ip_record = forms.ModelMultipleChoiceField( queryset=IpRecord.objects.filter(status=1).order_by('id'),label=_('IP'), required=False, widget=forms.SelectMultiple(attrs={'class':'form-control'}))
    manufacturer = newChoiceField(choices=(), label=_('Manufacturer'), required=False, widget=forms.Select(attrs={'class':'form-control'}))
    brand = newChoiceField(choices=(), label=_('Brand'), required=False, widget=forms.Select(attrs={'class':'form-control'}))
    idc_device_num = forms.CharField(max_length=255, required=False, label=_('Idc Device num'), widget=forms.TextInput(attrs={'class':'form-control'}))
    volume = forms.IntegerField( label=_('Volume'), required=False,  widget=forms.TextInput(attrs={'class':'form-control'}))
    model_num = forms.CharField(max_length=255, label=_('Model'), widget=forms.TextInput(attrs={'class':'form-control'}))
    serial = forms.CharField(max_length=255, label=_('Serial'), widget=forms.TextInput(attrs={'class':'form-control'}))
    asset_num = forms.CharField(max_length=255, label=_('Asset num'), required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    order_num = forms.CharField(max_length=255, label=_('Order num'), required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.IntegerField(label=_('Price'), required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    order_date = forms.CharField(max_length=255, label=_('Order date'), required=False, widget=newDateTimeInput(d_type='onlydate', attrs={'class':'form-control'}))
    warranty_period = forms.CharField(max_length=255, label=_('Warranty period'), required=False, widget=newDateTimeInput(d_type='onlydate', attrs={'class':'form-control'}))
    processor = forms.CharField(max_length=255, label=_('Processor'), required=False,  widget=forms.TextInput(attrs={'class':'form-control'}))
    memory = forms.CharField(max_length=255, label=_('Memory'), required=False,  widget=forms.TextInput(attrs={'class':'form-control'}))
    harddisk = forms.CharField(max_length=255, label=_('Harddisk'), required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    contrl_card = forms.CharField(max_length=255, label=_('Contrl card'), required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    network_card = forms.CharField(max_length=255, label=_('Network card'), required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    operating_system = forms.CharField(max_length=255, label=_('Operating System'), required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    comment = forms.CharField(max_length=255, label=_('Comment'), required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    status = newChoiceField(choices=(), label=_('Status'), required=False, widget=forms.Select(attrs={'class':'form-control'}))
    is_run = newChoiceField(choices=(), label=_('Is run'), required=False, widget=forms.Select(attrs={'class':'form-control'}))
    is_control_card = newChoiceField(choices=(), label=_('Is control card'), required=False, widget=forms.Select(attrs={'class':'form-control'}))
    is_virtualization = newChoiceField(choices=(), label=_('Is virtualization'), required=False, widget=forms.Select(attrs={'class':'form-control'}))
    is_dynamic = newChoiceField(choices=(), label=_('Is dynamic'), required=False, widget=forms.Select(attrs={'class':'form-control'}))
    is_deleted = newChoiceField(choices=(), label=_('Is deleted'), required=False, widget=forms.Select(attrs={'class':'form-control'}))


