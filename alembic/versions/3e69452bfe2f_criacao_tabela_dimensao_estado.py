"""criacao tabela dimensao estado

Revision ID: 3e69452bfe2f
Revises: 47b74fc1688d
Create Date: 2022-10-29 11:29:18.378345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e69452bfe2f'
down_revision = '47b74fc1688d'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table(
        'estado',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, comment="Id (Surrogate Key)"),
        sa.Column('ibge', sa.Integer, unique=True, nullable=False, comment="IBGE (Natural Key)"),
        sa.Column('sigla', sa.String, nullable=False, comment="Sigla"),
        sa.Column('nome', sa.String, nullable=False, comment="Nome"),
        sa.Column('latitude', sa.Float, nullable=False, comment="Latitude"),
        sa.Column('longitude', sa.Float, nullable=False, comment="Longitude"),
        sa.Column('regiao', sa.String, nullable=False, comment="Região"),
        comment="Dimensão Estado",
    )


def downgrade() -> None:
    op.drop_table('estado')
