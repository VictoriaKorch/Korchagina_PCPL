from notification_system import (
    EmailNotificationCreator, 
    SMSNotificationCreator, 
    PushNotificationCreator
)

def demo_notification_system():
    """Демонстрация работы системы уведомлений"""
    print("=== Демонстрация системы уведомлений ===")
    
    # Создаем создателей
    email_creator = EmailNotificationCreator("user@example.com")
    sms_creator = SMSNotificationCreator("+79991234567")
    push_creator = PushNotificationCreator("device_android_123")
    
    # Отправляем уведомления через создателей
    print("\n1. Отправка email уведомления:")
    email_creator.send_notification("Добро пожаловать в наше приложение!")
    
    print("\n2. Отправка SMS уведомления:")
    sms_creator.send_notification("Ваш код подтверждения: 5678")
    
    print("\n3. Отправка push уведомления:")
    push_creator.send_notification("У вас новое сообщение")
    
    print("\n=== Демонстрация завершена ===")

def demo_factory_method():
    """Демонстрация работы фабричного метода"""
    print("\n=== Демонстрация паттерна Фабричный метод ===")
    
    # Показываем, что разные создатели создают разные типы уведомлений
    creators = [
        EmailNotificationCreator("admin@company.com"),
        SMSNotificationCreator("+78005553535"),
        PushNotificationCreator("ios_device_456")
    ]
    
    for i, creator in enumerate(creators, 1):
        notification = creator.create_notification()
        print(f"{i}. Создатель: {creator.__class__.__name__}")
        print(f"   Создал: {notification.__class__.__name__}")
        print(f"   Отправка: {notification.send('Test message')}")

if __name__ == "__main__":
    demo_notification_system()
    demo_factory_method()