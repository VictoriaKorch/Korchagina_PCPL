import unittest
from notification_system import (
    EmailNotification, SMSNotification, PushNotification,
    EmailNotificationCreator, SMSNotificationCreator, PushNotificationCreator
)

class TestNotificationSystemBDD(unittest.TestCase):
    """
    BDD тесты в стиле Given-When-Then без использования feature файлов
    """
    
    def test_email_notification_creation_flow(self):
        """
        BDD Сценарий: Создание email уведомления
        Given пользователь имеет email адрес
        When создается email уведомление
        Then должен быть создан корректный объект email уведомления
        """
        # Given - дано
        user_email = "user@example.com"
        
        # When - когда
        creator = EmailNotificationCreator(user_email)
        notification = creator.create_notification()
        
        # Then - тогда
        self.assertIsInstance(notification, EmailNotification)
        self.assertEqual(notification.email, user_email)
    
    def test_sms_notification_creation_flow(self):
        """
        BDD Сценарий: Создание SMS уведомления
        Given пользователь имеет номер телефона
        When создается SMS уведомление
        Then должен быть создан корректный объект SMS уведомления
        """
        # Given
        user_phone = "+79991234567"
        
        # When
        creator = SMSNotificationCreator(user_phone)
        notification = creator.create_notification()
        
        # Then
        self.assertIsInstance(notification, SMSNotification)
        self.assertEqual(notification.phone, user_phone)
    
    def test_push_notification_creation_flow(self):
        """
        BDD Сценарий: Создание push уведомления
        Given пользователь имеет device ID
        When создается push уведомление
        Then должен быть создан корректный объект push уведомления
        """
        # Given
        device_id = "android_device_123"
        
        # When
        creator = PushNotificationCreator(device_id)
        notification = creator.create_notification()
        
        # Then
        self.assertIsInstance(notification, PushNotification)
        self.assertEqual(notification.device_id, device_id)
    
    def test_email_notification_send_flow(self):
        """
        BDD Сценарий: Отправка email уведомления
        Given есть создатель email уведомлений
        When отправляется сообщение через создателя
        Then сообщение должно быть успешно отправлено
        """
        # Given
        creator = EmailNotificationCreator("user@example.com")
        test_message = "Добро пожаловать в наше приложение!"
        
        # When
        result = creator.send_notification(test_message)
        
        # Then
        self.assertTrue(result)
    
    def test_sms_notification_send_flow(self):
        """
        BDD Сценарий: Отправка SMS уведомления
        Given есть создатель SMS уведомлений
        When отправляется сообщение через создателя
        Then сообщение должно быть успешно отправлено
        """
        # Given
        creator = SMSNotificationCreator("+79991234567")
        test_message = "Ваш код подтверждения: 1234"
        
        # When
        result = creator.send_notification(test_message)
        
        # Then
        self.assertTrue(result)
    
    def test_complete_notification_workflow(self):
        """
        BDD Сценарий: Полный workflow системы уведомлений
        Given система имеет несколько типов создателей уведомлений
        When создаются и отправляются разные типы уведомлений
        Then все уведомления должны быть корректно созданы и отправлены
        """
        # Given
        email_creator = EmailNotificationCreator("user@example.com")
        sms_creator = SMSNotificationCreator("+79991234567")
        push_creator = PushNotificationCreator("android_device_123")
        
        email_message = "Email уведомление"
        sms_message = "SMS уведомление"
        push_message = "Push уведомление"
        
        # When
        email_notification = email_creator.create_notification()
        sms_notification = sms_creator.create_notification()
        push_notification = push_creator.create_notification()
        
        email_result = email_notification.send(email_message)
        sms_result = sms_notification.send(sms_message)
        push_result = push_notification.send(push_message)
        
        # Then
        self.assertIsInstance(email_notification, EmailNotification)
        self.assertIsInstance(sms_notification, SMSNotification)
        self.assertIsInstance(push_notification, PushNotification)
        
        self.assertTrue(email_result)
        self.assertTrue(sms_result)
        self.assertTrue(push_result)
        
        self.assertEqual(email_notification.email, "user@example.com")
        self.assertEqual(sms_notification.phone, "+79991234567")
        self.assertEqual(push_notification.device_id, "android_device_123")

class TestNotificationSystemBDDWithMocks(unittest.TestCase):
    """
    BDD тесты с использованием Mock объектов
    """
    
    def test_email_notification_with_mock_bdd(self):
        """
        BDD Сценарий: Тестирование email уведомления с mock
        Given есть mock объект для тестирования
        When выполняется отправка уведомления
        Then должны быть вызваны соответствующие методы mock объекта
        """
        # Given
        from unittest.mock import Mock
        mock_notification = Mock()
        mock_notification.send.return_value = True
        
        creator = EmailNotificationCreator("test@example.com")
        original_method = creator.create_notification
        creator.create_notification = Mock(return_value=mock_notification)
        
        test_message = "Test message"
        
        # When
        result = creator.send_notification(test_message)
        
        # Then
        self.assertTrue(result)
        creator.create_notification.assert_called_once()
        mock_notification.send.assert_called_once_with(test_message)
        
        # Восстанавливаем оригинальный метод
        creator.create_notification = original_method

if __name__ == "__main__":
    unittest.main(verbosity=2)