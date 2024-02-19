# Устанавливаем базовый образ, содержащий JDK
FROM openjdk:latest
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /usr/src/app
# Копируем исходный код приложения внутрь контейнера
COPY ./src .
COPY ./lib .
# Компилируем Java исходный код
RUN javac -sourcepath . -d out ./homework/Main.java
# Теперь рабочая директория - директория с файлами .class
WORKDIR /usr/src/app/out
ENTRYPOINT ["java","homework/Main.java"]