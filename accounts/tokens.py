from django.contrib.auth.tokens import PasswordResetTokenGenerator


class ConfirmEmailTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(user.is_active) + str(timestamp)


confirmation_email_token_generator = ConfirmEmailTokenGenerator()
