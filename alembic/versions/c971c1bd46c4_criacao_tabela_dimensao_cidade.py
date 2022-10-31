"""criacao tabela dimensao cidade

Revision ID: c971c1bd46c4
Revises: 3e69452bfe2f
Create Date: 2022-10-29 11:34:35.454947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c971c1bd46c4'
down_revision = '3e69452bfe2f'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table(
        'cidade',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, comment="Id (Surrogate Key)"),
        sa.Column('estado_id', sa.Integer, nullable=False, comment="Estado (Surrogate Key)"),
        sa.Column('ibge', sa.Integer, unique=True, nullable=False, comment="IBGE (Natural Key)"),
        sa.Column('nome', sa.String, nullable=False, comment="Nome"),
        sa.Column('capital', sa.Boolean, nullable=False, comment="Capital (Sim/Não)"),
        sa.Column('latitude', sa.Float, nullable=False, comment="Latitude"),
        sa.Column('longitude', sa.Float, nullable=False, comment="Longitude"),
        sa.ForeignKeyConstraint(['estado_id'], ['estado.id'], name='fk_cidade_estado_id'),
        comment="Dimensão Cidade",
    )


def downgrade() -> None:
    op.drop_table('cidade')
