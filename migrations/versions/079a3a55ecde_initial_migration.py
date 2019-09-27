"""Initial Migration

Revision ID: 079a3a55ecde
Revises: 5a8ecfc5df6e
Create Date: 2019-09-26 11:39:14.582470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '079a3a55ecde'
down_revision = '5a8ecfc5df6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('name', sa.String(length=255), nullable=True))
    op.add_column('posts', sa.Column('gender', sa.String(length=255), nullable=True))
    op.add_column('posts', sa.Column('name', sa.String(length=255), nullable=True))
    op.drop_column('posts', 'title')
    op.drop_column('posts', 'category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('posts', sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('posts', 'name')
    op.drop_column('posts', 'gender')
    op.drop_column('comments', 'name')
    # ### end Alembic commands ###