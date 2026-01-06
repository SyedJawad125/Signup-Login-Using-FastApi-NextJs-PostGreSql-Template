"""initial

Revision ID: d9f2c963cf6a
Revises: 
Create Date: 2026-01-06 16:52:06.660975

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9f2c963cf6a'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    
    # Step 1: Create tables WITHOUT foreign keys that cause circular dependencies
    
    # Create users table without employee_id and role_id foreign keys
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), server_default='TRUE', nullable=False),
        sa.Column('is_superuser', sa.Boolean(), server_default='FALSE', nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=True),
        sa.Column('employee_id', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('deleted', sa.Boolean(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('employee_id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    
    # Create employees table without user tracking foreign keys
    op.create_table('employees',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=50), nullable=False),
        sa.Column('last_name', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=100), nullable=False),
        sa.Column('phone_number', sa.String(length=20), nullable=True),
        sa.Column('hire_date', sa.Date(), nullable=False),
        sa.Column('job_title', sa.String(length=100), nullable=False),
        sa.Column('salary', sa.Float(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('deleted', sa.Boolean(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_by_user_id', sa.Integer(), nullable=True),
        sa.Column('updated_by_user_id', sa.Integer(), nullable=True),
        sa.Column('deleted_by_user_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employees_email'), 'employees', ['email'], unique=True)
    op.create_index(op.f('ix_employees_id'), 'employees', ['id'], unique=False)
    
    # Create roles table without user tracking foreign keys
    op.create_table('roles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('code', sa.String(length=50), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('deleted', sa.Boolean(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_by_user_id', sa.Integer(), nullable=True),
        sa.Column('updated_by_user_id', sa.Integer(), nullable=True),
        sa.Column('deleted_by_user_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_roles_id'), 'roles', ['id'], unique=False)
    
    # Create imagecategories table without user tracking foreign keys
    op.create_table('imagecategories',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('category', sa.String(length=50), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('deleted', sa.Boolean(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_by_user_id', sa.Integer(), nullable=True),
        sa.Column('updated_by_user_id', sa.Integer(), nullable=True),
        sa.Column('deleted_by_user_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_imagecategories_id'), 'imagecategories', ['id'], unique=False)
    
    # Create permissions table without user tracking foreign keys
    op.create_table('permissions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('code', sa.String(length=50), nullable=False),
        sa.Column('module_name', sa.String(length=50), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('deleted', sa.Boolean(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_by_user_id', sa.Integer(), nullable=True),
        sa.Column('updated_by_user_id', sa.Integer(), nullable=True),
        sa.Column('deleted_by_user_id', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_permissions_id'), 'permissions', ['id'], unique=False)
    
    # Step 2: Add foreign key constraints now that all tables exist
    
    # Add foreign keys to users table
    op.create_foreign_key('fk_users_employee_id', 'users', 'employees', ['employee_id'], ['id'])
    op.create_foreign_key('fk_users_role_id', 'users', 'roles', ['role_id'], ['id'])
    
    # Add foreign keys to employees table
    op.create_foreign_key('fk_employees_created_by', 'employees', 'users', ['created_by_user_id'], ['id'])
    op.create_foreign_key('fk_employees_updated_by', 'employees', 'users', ['updated_by_user_id'], ['id'])
    op.create_foreign_key('fk_employees_deleted_by', 'employees', 'users', ['deleted_by_user_id'], ['id'])
    
    # Add foreign keys to roles table
    op.create_foreign_key('fk_roles_created_by', 'roles', 'users', ['created_by_user_id'], ['id'])
    op.create_foreign_key('fk_roles_updated_by', 'roles', 'users', ['updated_by_user_id'], ['id'])
    op.create_foreign_key('fk_roles_deleted_by', 'roles', 'users', ['deleted_by_user_id'], ['id'])
    
    # Add foreign keys to imagecategories table
    op.create_foreign_key('fk_imagecategories_created_by', 'imagecategories', 'users', ['created_by_user_id'], ['id'])
    op.create_foreign_key('fk_imagecategories_updated_by', 'imagecategories', 'users', ['updated_by_user_id'], ['id'])
    op.create_foreign_key('fk_imagecategories_deleted_by', 'imagecategories', 'users', ['deleted_by_user_id'], ['id'])
    
    # Add foreign keys to permissions table
    op.create_foreign_key('fk_permissions_created_by', 'permissions', 'users', ['created_by_user_id'], ['id'])
    op.create_foreign_key('fk_permissions_updated_by', 'permissions', 'users', ['updated_by_user_id'], ['id'])
    op.create_foreign_key('fk_permissions_deleted_by', 'permissions', 'users', ['deleted_by_user_id'], ['id'])
    
    # Step 3: Create dependent tables (with foreign keys)
    
    # Create images table
    op.create_table('images',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=30), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('image_path', sa.String(length=255), nullable=False),
        sa.Column('category_id', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('deleted', sa.Boolean(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_by_user_id', sa.Integer(), nullable=True),
        sa.Column('updated_by_user_id', sa.Integer(), nullable=True),
        sa.Column('deleted_by_user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['category_id'], ['imagecategories.id'], ),
        sa.ForeignKeyConstraint(['created_by_user_id'], ['users.id'], ),
        sa.ForeignKeyConstraint(['deleted_by_user_id'], ['users.id'], ),
        sa.ForeignKeyConstraint(['updated_by_user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_images_id'), 'images', ['id'], unique=False)
    
    # Create association tables
    op.create_table('user_role',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('user_id', 'role_id')
    )
    
    op.create_table('role_permission',
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.Column('permission_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['permission_id'], ['permissions.id'], ),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
        sa.PrimaryKeyConstraint('role_id', 'permission_id')
    )
    
    op.create_table('user_permission',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('permission_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['permission_id'], ['permissions.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('user_id', 'permission_id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    
    # Drop in reverse order
    op.drop_table('user_permission')
    op.drop_table('role_permission')
    op.drop_table('user_role')
    
    op.drop_index(op.f('ix_images_id'), table_name='images')
    op.drop_table('images')
    
    # Drop foreign keys before dropping tables
    op.drop_constraint('fk_permissions_deleted_by', 'permissions', type_='foreignkey')
    op.drop_constraint('fk_permissions_updated_by', 'permissions', type_='foreignkey')
    op.drop_constraint('fk_permissions_created_by', 'permissions', type_='foreignkey')
    
    op.drop_constraint('fk_imagecategories_deleted_by', 'imagecategories', type_='foreignkey')
    op.drop_constraint('fk_imagecategories_updated_by', 'imagecategories', type_='foreignkey')
    op.drop_constraint('fk_imagecategories_created_by', 'imagecategories', type_='foreignkey')
    
    op.drop_constraint('fk_roles_deleted_by', 'roles', type_='foreignkey')
    op.drop_constraint('fk_roles_updated_by', 'roles', type_='foreignkey')
    op.drop_constraint('fk_roles_created_by', 'roles', type_='foreignkey')
    
    op.drop_constraint('fk_employees_deleted_by', 'employees', type_='foreignkey')
    op.drop_constraint('fk_employees_updated_by', 'employees', type_='foreignkey')
    op.drop_constraint('fk_employees_created_by', 'employees', type_='foreignkey')
    
    op.drop_constraint('fk_users_role_id', 'users', type_='foreignkey')
    op.drop_constraint('fk_users_employee_id', 'users', type_='foreignkey')
    
    # Drop tables
    op.drop_index(op.f('ix_permissions_id'), table_name='permissions')
    op.drop_table('permissions')
    
    op.drop_index(op.f('ix_imagecategories_id'), table_name='imagecategories')
    op.drop_table('imagecategories')
    
    op.drop_index(op.f('ix_roles_id'), table_name='roles')
    op.drop_table('roles')
    
    op.drop_index(op.f('ix_employees_id'), table_name='employees')
    op.drop_index(op.f('ix_employees_email'), table_name='employees')
    op.drop_table('employees')
    
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')