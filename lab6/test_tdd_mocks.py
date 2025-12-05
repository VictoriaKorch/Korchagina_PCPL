import unittest
from unittest.mock import Mock, patch
from notification_system import (
    EmailNotification, SMSNotification, PushNotification,
    EmailNotificationCreator, SMSNotificationCreator, PushNotificationCreator,
    Notification
)

class TestNotificationSystemTDD(unittest.TestCase):
    
    def test_email_notification_creation(self):
        """TDD: Тест создания email уведомления"""
        email = "test@example.com"
        notification = EmailNotification(email)
        self.assertEqual(notification.email, email)
    
    def test_sms_notification_creation(self):
        """TDD: Тест создания SMS уведомления"""
        phone = "+1234567890"
        notification = SMSNotification(phone)
        self.assertEqual(notification.phone, phone)
    
    def test_push_notification_creation(self):
        """TDD: Тест создания push уведомления"""
        device_id = "device123"
        notification = PushNotification(device_id)
        self.assertEqual(notification.device_id, device_id)
    
    def test_email_creator_creates_correct_type(self):
        """TDD: Тест что EmailCreator создает правильный тип"""
        creator = EmailNotificationCreator("test@example.com")
        notification = creator.create_notification()
        self.assertIsInstance(notification, EmailNotification)
    
    def test_sms_creator_creates_correct_type(self):
        """TDD: Тест что SMSCreator создает правильный тип"""
        creator = SMSNotificationCreator("+1234567890")
        notification = creator.create_notification()
        self.assertIsInstance(notification, SMSNotification)
    
    def test_push_creator_creates_correct_type(self):
        """TDD: Тест что PushCreator создает правильный тип"""
        creator = PushNotificationCreator("device123")
        notification = creator.create_notification()
        self.assertIsInstance(notification, PushNotification)
    
    @patch('notification_system.EmailNotification.send')
    def test_email_notification_send_with_mock(self, mock_send):
        """TDD: Тест отправки email с mock объектом"""
        mock_send.return_value = True
        creator = EmailNotificationCreator("test@example.com")
        result = creator.send_notification("Test message")
        
        self.assertTrue(result)
        mock_send.assert_called_once_with("Test message")

class TestNotificationSystemWithMocks(unittest.TestCase):
    
    def test_notification_send_with_mock(self):
        """Mock: Тест с использованием Mock объекта"""
        # Создаем mock объект уведомления
        mock_notification = Mock(spec=Notification)
        mock_notification.send.return_value = True
        
        # Создаем mock создателя, который возвращает наш mock уведомления
        mock_creator = Mock()
        mock_creator.create_notification.return_value = mock_notification
        mock_creator.send_notification = lambda msg: mock_creator.create_notification().send(msg)
        
        # Тестируем
        result = mock_creator.send_notification("Test message")
        
        # Проверяем
        self.assertTrue(result)
        mock_creator.create_notification.assert_called_once()
        mock_notification.send.assert_called_once_with("Test message")
    
    @patch('notification_system.SMSNotification')
    def test_sms_creator_with_patch(self, mock_sms_class):
        """Mock: Тест SMS создателя с patch"""
        # Настраиваем mock
        mock_instance = Mock()
        mock_instance.send.return_value = True
        mock_sms_class.return_value = mock_instance
        
        # Тестируем
        creator = SMSNotificationCreator("+1234567890")
        result = creator.send_notification("Test SMS")
        
        # Проверяем
        self.assertTrue(result)
        mock_sms_class.assert_called_once_with("+1234567890")
        mock_instance.send.assert_called_once_with("Test SMS")
    
    def test_factory_method_pattern_with_mocks(self):
        """Mock: Комплексный тест фабричного метода с моками"""
        # Создаем несколько mock уведомлений
        email_mock = Mock()
        email_mock.send.return_value = True
        
        sms_mock = Mock()
        sms_mock.send.return_value = True
        
        # Создаем создателей с подменой метода создания
        email_creator = EmailNotificationCreator("test@example.com")
        email_creator.create_notification = Mock(return_value=email_mock)
        
        sms_creator = SMSNotificationCreator("+1234567890")
        sms_creator.create_notification = Mock(return_value=sms_mock)
        
        # Тестируем отправку через разных создателей
        email_result = email_creator.send_notification("Email message")
        sms_result = sms_creator.send_notification("SMS message")
        
        # Проверяем результаты
        self.assertTrue(email_result)
        self.assertTrue(sms_result)
        email_mock.send.assert_called_once_with("Email message")
        sms_mock.send.assert_called_once_with("SMS message")

if __name__ == "__main__":
    unittest.main(verbosity=2)