"""criacao tabela dimensao tempo

Revision ID: 47b74fc1688d
Revises: 
Create Date: 2022-10-29 11:08:24.932631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47b74fc1688d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
	op.create_table(
		'tempo',
		sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, comment="Id (Surrogate Key)"),
		sa.Column('data', sa.Date, unique=True, nullable=False, comment="Data (Natural Key)"),
		sa.Column('dia', sa.Integer, nullable=False, comment="Dia"),
		sa.Column('mes', sa.Integer, nullable=False, comment="Mês"),
		sa.Column('ano', sa.Integer, nullable=False, comment="Ano"),
		sa.Column('bimestre', sa.Integer, nullable=False, comment="Bimestre"),
		sa.Column('trimestre', sa.Integer, nullable=False, comment="Trimestre"),
		sa.Column('semestre', sa.Integer, nullable=False, comment="Semestre"),
		sa.Column('estacao', sa.String, nullable=False, comment="Estação do Ano"),
    comment="Dimensão Tempo"
	)


def downgrade() -> None:
    op.drop_table('tempo')
