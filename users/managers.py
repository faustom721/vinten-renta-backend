from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, ci, password, first_name, last_name, email, phone, is_active):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            ci=ci,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            is_active=is_active
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user
