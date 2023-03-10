"""last

Revision ID: e0911cdf9fb3
Revises: b9691f7517a7
Create Date: 2022-12-21 20:50:03.828403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0911cdf9fb3'
down_revision = 'b9691f7517a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.String(), nullable=True))
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=200),
               existing_nullable=False)
        batch_op.create_foreign_key(batch_op.f('fk_book_category_id_category'), 'category', ['category_id'], ['id'])
        batch_op.drop_column('category')

    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=200),
               existing_nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=200),
               existing_nullable=False)
        batch_op.create_unique_constraint(batch_op.f('uq_user_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_username'), ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_username'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_email'), type_='unique')
        batch_op.alter_column('id',
               existing_type=sa.String(length=200),
               type_=sa.INTEGER(),
               existing_nullable=False)
        batch_op.drop_column('created_at')

    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.String(length=200),
               type_=sa.INTEGER(),
               existing_nullable=False)
        batch_op.drop_column('created_at')

    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.VARCHAR(length=120), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_book_category_id_category'), type_='foreignkey')
        batch_op.alter_column('id',
               existing_type=sa.String(length=200),
               type_=sa.INTEGER(),
               existing_nullable=False)
        batch_op.drop_column('category_id')

    # ### end Alembic commands ###
