"""foreign key

Revision ID: bda4c3272216
Revises: b4e41f6e2605
Create Date: 2022-12-21 18:54:48.709108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bda4c3272216'
down_revision = 'b4e41f6e2605'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.String(), nullable=True))
        batch_op.create_foreign_key(None, 'category', ['category_id'], ['id'])
        batch_op.drop_column('category')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.VARCHAR(length=120), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('category_id')

    # ### end Alembic commands ###
