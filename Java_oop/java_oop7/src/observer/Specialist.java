package observer;

public class Specialist implements Observer {

    // region Private Fields

    private final String name;
    private final String vacancyWorker = "Administrator";
    private int salary = 80000;

    private String companyName;

    private boolean specialistStatus = true;

    // endregion

    public Specialist(String name) {
        this.name = name;
    }

    // region Getters and Setters

    public String getVacancyWorker() {
        return vacancyWorker;
    }

    public String getName() {
        return name;
    }

    public boolean isWorkerStatus() {
        return specialistStatus;
    }

    public int getSalary() {
        return salary;
    }

    public String getCompanyName() {
        return companyName;
    }

    // endregion

    @Override
    public void receiveOffer(String nameCompany, String companyVacancy, int salary) {
        if (this.salary <= salary && this.vacancyWorker.equals(companyVacancy)) {
            System.out.printf("Специалист %s %s: Мне нужна эта работа! (компания: %s, вакансия: %s, заработная плата: %d)\n",
                    vacancyWorker, name, nameCompany, companyVacancy, salary);
            this.salary = salary;
            companyName = nameCompany;
            specialistStatus = false;
        } else {
            System.out.printf("Специалист %s %s: Я найду работу получше! (компания: %s, вакансия: %s, заработная плата: %d)\n",
                    vacancyWorker, name, nameCompany, companyVacancy, salary);
        }
    }

}
