from rest_framework import serializers
from app.projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id','procore_index', 'pjm_index', 'system_of_origin', 'project', 'project_number', 'project_description', 'address', 'city', 'state', 'zip', 'latitude', 'longitude', 'project_stage', 'phone', 'created', 'last_updated', 'procore_status', 'sage_status', 'project_status', 'Construction_Type', 'product_type', 'size', 'estimated_start', 'revised_start', 'actual_start', 'estimated_completion', 'revised_completion', 'actual_completion', 'customer_id', 'customer_name', 'architect', 'division', 'contract_type', 'team_leader', 'project_managers', 'superintendents', 'original_contract_value', 'approved_contract_changes', 'revised_contract_value', 'jtd_work_billed', 'jtd_retainage_held', 'jtd_payments_received', 'original_estimated_cost', 'approved_estimate_changes', 'revised_estimated_cost', 'original_committed_cost', 'approved_commitment_changes', 'revised_committed_cost', 'jtd_cost', 'jtd_payments_made', 'projected_post', 'original_gp', 'projected_gp', 'original_gp_percent', 'projected_gp_percent', 'gain_fade', 'gain_fade_percent', 'database_stamp','is_deleted','created_at','updated_at')
        