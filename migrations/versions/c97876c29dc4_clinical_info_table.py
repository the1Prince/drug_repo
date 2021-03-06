"""clinical_info table

Revision ID: c97876c29dc4
Revises: 
Create Date: 2022-03-15 10:38:46.195791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c97876c29dc4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clinical_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cli_id', sa.String(length=64), nullable=True),
    sa.Column('indication', sa.Text(), nullable=True),
    sa.Column('dosage', sa.Text(), nullable=True),
    sa.Column('administration', sa.Text(), nullable=True),
    sa.Column('contrindication', sa.Text(), nullable=True),
    sa.Column('interaction', sa.Text(), nullable=True),
    sa.Column('fertility', sa.Text(), nullable=True),
    sa.Column('warning_precaution', sa.Text(), nullable=True),
    sa.Column('adverse_reaction', sa.Text(), nullable=True),
    sa.Column('drug_id', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('clinical_trial_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('clinical_info_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('description',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('color', sa.String(length=64), nullable=True),
    sa.Column('gram', sa.Float(), nullable=True),
    sa.Column('shape', sa.String(length=128), nullable=True),
    sa.Column('extra_details', sa.Text(), nullable=True),
    sa.Column('drug_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('drug',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('barcode', sa.String(length=64), nullable=True),
    sa.Column('qrcode', sa.String(length=128), nullable=True),
    sa.Column('img', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_drug_name'), 'drug', ['name'], unique=True)
    op.create_table('manufacturer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.Column('drug_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('non_clinical_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('carcinogenicity_mutagenicity', sa.Text(), nullable=True),
    sa.Column('reproductive_toxicology', sa.Text(), nullable=True),
    sa.Column('feritlity', sa.Text(), nullable=True),
    sa.Column('drug_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('overdose',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('signs_symptoms', sa.Text(), nullable=True),
    sa.Column('treatment', sa.Text(), nullable=True),
    sa.Column('clinical_info_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pharmaceutical_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('list_of_excipients', sa.Text(), nullable=True),
    sa.Column('storage_conditions', sa.Text(), nullable=True),
    sa.Column('nature_content_ofContainer', sa.Text(), nullable=True),
    sa.Column('instruction_for_handling', sa.Text(), nullable=True),
    sa.Column('instruction_for_disposal', sa.Text(), nullable=True),
    sa.Column('text_revision_date', sa.Text(), nullable=True),
    sa.Column('drug_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pharmacodynamic_properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('mechanism_of_action', sa.Text(), nullable=True),
    sa.Column('drug_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pharmacokinetic_properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('absorption', sa.Text(), nullable=True),
    sa.Column('distribution', sa.Text(), nullable=True),
    sa.Column('metabolism', sa.Text(), nullable=True),
    sa.Column('elimination', sa.Text(), nullable=True),
    sa.Column('steady_state_pharmacokinetics', sa.Text(), nullable=True),
    sa.Column('drug_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('special_population',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('clinical_info_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('telephone', sa.String(length=15), nullable=True),
    sa.Column('token', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('special_population')
    op.drop_table('pharmacokinetic_properties')
    op.drop_table('pharmacodynamic_properties')
    op.drop_table('pharmaceutical_info')
    op.drop_table('overdose')
    op.drop_table('non_clinical_info')
    op.drop_table('manufacturer')
    op.drop_index(op.f('ix_drug_name'), table_name='drug')
    op.drop_table('drug')
    op.drop_table('description')
    op.drop_table('clinical_trial_data')
    op.drop_table('clinical_info')
    # ### end Alembic commands ###
