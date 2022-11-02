"""criacao tabela dimensao profissional

Revision ID: 5a107dec7b5d
Revises: a9c0119d15c4
Create Date: 2022-11-02 20:34:53.650490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a107dec7b5d'
down_revision = 'a9c0119d15c4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'profissional',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, comment="Id (Surrogate Key)"),
        sa.Column('codigo', sa.Integer, unique=True, nullable=False, comment="Código (Natural Key)"),
        sa.Column('nome', sa.String, nullable=False, comment="Nome"),
        sa.Column('cpf', sa.String, nullable=False, comment="CPF"),
        sa.Column('conselho_numero', sa.String, nullable=False, comment="Registro Conselho"),
        sa.Column('conselho_sigla', sa.String, nullable=False, comment="Sigla Conselho"),
        sa.Column('conselho_uf', sa.String, nullable=False, comment="Estado Conselho"),
        comment="Dimensão Profissional",
    )


def downgrade() -> None:
    op.drop_table('profissional')
