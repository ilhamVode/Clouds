# Лабораторная работа 2. Сравнение сервисов Amazon Web Services и Microsoft Azure

**Вариант:** 4  
**Выполнил:** Гашимов Ильхам Фаррух оглы

## Цель
Научиться анализировать облачные сервисы без привязки к вендору. Создать единую модель для классификации сервисов AWS и Azure.

## Исходные данные
1. Результаты Лабораторной работы 1 (файл `fulled_4_variant_1.csv`)
2. Данные биллинга Microsoft Azure
3. Образец структуры для классификации


### 1. Анализ данных
- Изучены данные биллинга Azure
- Найдены соответствия между сервисами AWS и Azure

### 2. Создание модели
Создана единая иерархическая модель:

1. **IT Tower** (Compute, Networking, Database, Analytics)
2. **Service Family** (Serverless, Containers, Managed Database)
3. **Service Type** (AWS Lambda, Azure Functions)
4. **Service Sub Type** (вариант сервиса)
5. **Service Usage Type** (метрика потребления)

### 3. Классификация Azure
Для каждого сервиса Azure:
- Определен IT Tower
- Выбрана Service Family
- Указан Service Type и Sub Type
- Определен Service Usage Type

### 4. Проверка
- Использованы те же принципы, что в ЛР1
- Сохранена логика классификации
- Сохранена детализация от общего к частному

## Примеры

### Контейнерные сервисы
- **AWS**: ECS/EKS → Compute → Containers
- **Azure**: Container Instances → Compute → Containers

### Управляемые базы данных
- **AWS**: RDS → Database → Managed Database
- **Azure**: Azure Database for MySQL → Database → Managed Database

## Результаты

### Достигнуто:
1. Создана единая модель для AWS и Azure
2. Реализована иерархическая структура
3. Обеспечена сопоставимость сервисов

### Выводы:
1. AWS и Azure предлагают похожие сервисы
2. Универсальная классификация возможна

**Итог:** Создана единая модель для классификации сервисов AWS и Azure. Получены навыки анализа облачных сервисов без привязки к вендору.