"""criacao tabela dimensao produto

Revision ID: a9c0119d15c4
Revises: c971c1bd46c4
Create Date: 2022-10-31 21:41:12.285217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9c0119d15c4'
down_revision = 'c971c1bd46c4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'produto',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True, comment="Id (Surrogate Key)"),
        sa.Column('codigo', sa.Integer, unique=True, nullable=False, comment="Código (Natural Key)"),
        sa.Column('nome', sa.String, nullable=False, comment="Nome"),
        sa.Column('registro', sa.String, comment="Registro ANS"),
        sa.Column('tipo', sa.String, nullable=False, comment="Tipo do Produto"),
        sa.Column('abrangencia', sa.String, nullable=False, comment="Abrangência"),
        sa.Column('segmentacao', sa.String, nullable=False, comment="Segmentação"),
        sa.Column('acomodacao', sa.String, nullable=False, comment="Acomodação"),
        comment="Dimensão Produto"
    )


def downgrade() -> None:
    op.drop_table('produto')
