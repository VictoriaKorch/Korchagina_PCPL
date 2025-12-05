from abc import ABC, abstractmethod
from typing import Protocol

# Интерфейс для уведомлений
class Notification(Protocol):
    def send(self, message: str) -> bool:
        ...

# Конкретные реализации уведомлений
class EmailNotification:
    def __init__(self, email: str):
        self.email = email
    
    def send(self, message: str) -> bool:
        print(f"Отправка email на {self.email}: {message}")
        return True

class SMSNotification:
    def __init__(self, phone: str):
        self.phone = phone
    
    def send(self, message: str) -> bool:
        print(f"Отправка SMS на {self.phone}: {message}")
        return True

class PushNotification:
    def __init__(self, device_id: str):
        self.device_id = device_id
    
    def send(self, message: str) -> bool:
        print(f"Отправка push на устройство {self.device_id}: {message}")
        return True

# Абстрактный создатель
class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass
    
    def send_notification(self, message: str) -> bool:
        notification = self.create_notification()
        return notification.send(message)

# Конкретные создатели
class EmailNotificationCreator(NotificationCreator):
    def __init__(self, email: str):
        self.email = email
    
    def create_notification(self) -> Notification:
        return EmailNotification(self.email)

class SMSNotificationCreator(NotificationCreator):
    def __init__(self, phone: str):
        self.phone = phone
    
    def create_notification(self) -> Notification:
        return SMSNotification(self.phone)

class PushNotificationCreator(NotificationCreator):
    def __init__(self, device_id: str):
        self.device_id = device_id
    
    def create_notification(self) -> Notification:
        return PushNotification(self.device_id)