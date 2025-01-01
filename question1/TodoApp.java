package question1;

import java.time.LocalDateTime;
import java.util.*;

public class TodoApp {
    static class Task{
        private int taskId;
        private LocalDateTime deadline;
        private String taskName;
        private LocalDateTime createdAt;
        private LocalDateTime completedAt;
        private boolean isCompleted;

        public Task(int taskId, String taskName, LocalDateTime deadline, LocalDateTime createdAt, boolean isCompleted){
            this.taskId=taskId;
            this.taskName=taskName;
            this.deadline=deadline;
            this.createdAt=LocalDateTime.now();
            this.isCompleted=false;
        }
        public int getTaskId() {
            return taskId;
        }
        public String getTaskName() {
            return taskName;
        }
        public LocalDateTime getDeadline() {
            return deadline;
        }
        public boolean isCompleted() {
            return isCompleted;
        }
        public void complete() {
            this.isCompleted=true;
            this.completedAt=LocalDateTime.now();
        }

        public void modify(String taskName, LocalDateTime deadline){
            if (taskName!= null){
                this.taskName=taskName;
            }
            if (deadline!=null){
                this.deadline=deadline;
            }
        }

        @Override
        public String toString() {
            return "Task ID: " + taskId + ", Task Name: " + taskName + ", Deadline: " + deadline + ", Completed: " + isCompleted;
        }
    }

    private Map<Integer, Task> tasks;
    private List<String> activityLog;
    public TodoApp() {
        this.tasks=new HashMap<>();
        this.activityLog=new ArrayList<>();
    }

    public void addTask(Task task) {
        tasks.put(task.getTaskId(), task);
        activityLog.add(LocalDateTime.now() + ", Task added: " + task.getTaskId());
    }

    public Task getTask(int taskId){
        return tasks.get(taskId);
    }

    public void modifyTask(int taskId, String taskName, LocalDateTime deadline){
        Task task=tasks.get(taskId);
        if (task!=null){
            task.modify(taskName, deadline);
            activityLog.add(LocalDateTime.now() + ", Task modified: " + taskId + "with task name: " + taskName);
        }
    }

    public void removeTask(int taskId){
        Task task=tasks.remove(taskId);
        if (task!=null){
            activityLog.add(LocalDateTime.now() + ", Task removed: " + taskId);
        }
    }

    public List<Task> listTasks(){
        List<Task> somethingList = new ArrayList<>();
        for(Task task:tasks.values()){
            somethingList.add(task);
        }
        return somethingList;
    }

    public Map<String, Integer> getStatistics(LocalDateTime startTime, LocalDateTime endTime){
        int added=0, completed=0, spilled=0;
        for(Task task:tasks.values()){
            if ((startTime == null || task.getDeadline().isAfter(startTime)) && (endTime == null || task.getDeadline().isBefore(endTime))) {
                added++;
                if (task.isCompleted()){
                    completed++;
                } else if (task.getDeadline().isBefore(LocalDateTime.now())) {
                    spilled++;
                }
            }
        }
        Map<String, Integer> stats = new HashMap<>();
        stats.put("Added: ", added);
        stats.put("Completed: ", completed);
        stats.put("Spilled: ", spilled);
        return stats;
    }

    public List<String> getActivityLog(LocalDateTime startTime, LocalDateTime endTime){
        return activityLog;
        // stream().filter(log -> {
        //     String[] parts = log.split(": ");
        //     LocalDateTime logTime = LocalDateTime.parse(parts[0], null);
        //     return (startTime == null || logTime.isAfter(startTime)) && (endTime == null || logTime.isBefore(endTime));
        // }).toList();
    }


    public static void main(String[] args){
        TodoApp app = new TodoApp();
        Task task1 = new Task(1, "taskName1", LocalDateTime.of(2025,1,10,12,0), LocalDateTime.now(), false);
        Task task2 = new Task(1, "taskName1", LocalDateTime.of(2025,1,5,18,0), LocalDateTime.now(), false);
        app.addTask(task1);
        app.addTask(task2);

        app.modifyTask(1, "task123", null);

        Task task = app.getTask(1);
        if (task!=null){
            task.complete();
        }
        System.out.println("Tasks: ");
        for (Task t: app.listTasks()){
            System.out.println(t.toString());
        }

        System.out.println("\nStats: ");
        System.out.println(app.getStatistics(null, null));

        System.out.println("\nActivity: ");
        for (String log: app.getActivityLog(null, null)){
            System.out.println(log);
        }

    }




}