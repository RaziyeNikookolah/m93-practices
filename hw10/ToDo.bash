clear
declare -a menu_array=(
                        "Add a new task" 
                        "Show undone task" 
                        "Set a task done and delete in undone list" 
                        "Show done tasks" 
                        "Delete a done task and add it to deleted tasks" 
                        "Show deleted tasks" 
                        "Search in lists (done, undone, deleted)" 
                        "Exit"
                    )
if ! [ -f ./done.txt ];then
    touch done.txt
    echo "Task Title   Task priority  Added Date,time    Done date,time ">>done.txt
    echo "------------------------------------------------------------------------------- ">>done.txt

fi
if ! [ -f ./undone.txt ];then
    touch undone.txt
    echo "Task Title   Task priority  Added Date,time  ">>undone.txt
    echo "---------------------------------------------">>undone.txt

fi
if ! [ -f ./deleted.txt ];then
    touch deleted.txt
    echo "Task Title   Task priority  Added Date,time    Done date,time  Deleted date,time">>deleted.txt
    echo "------------------------------------------------------------------------------- ">>deleted.txt
fi
while [ True ];do
    PS3="Choose an item : "
    select item in "${menu_array[@]}"
    do 
        case ${item} in 
            ${menu_array[0]})
            printf "Enter your new task name :\n"
            read task_name
            printf "Enter task priority:\n"
            read task_priority
            printf "Enter date:\n"
            read date
            printf "Enter time:\n"
            read time
            echo "$task_name      $task_priority      $date , $time">>undone.txt
            printf "\n\tAdded..\n"
            break
            ;;
            ${menu_array[1]})
            if [ ! -s ./undone.txt ]; then
                printf "\n\tNothing to display..\n"
            else
                cat undone.txt
                printf "\n\n"
            fi
            break
            ;;
            ${menu_array[2]})
                printf "Enter the task name :\n"
                read task_name
                printf "Enter the date of done  :\n"
                read done_date
                printf "Enter the time of done  :\n"
                read done_time
                cat undone.txt | grep "${task_name}"  | while read line
                    do                
                        echo "$line       $done_date , $done_time">>done.txt
                        sed -i "/$task_name/ d" undone.txt
                        printf "\tOperation done..\n"
                    done
                break
            ;;
            ${menu_array[3]})
                if [ ! -s ./done.txt ]; then
                    printf "\n\tNothing to display..\n"
                else      
                    cat done.txt 
                    printf "\n\n"
                fi
                break
            ;;
            ${menu_array[4]}) #Delete a done task and add it to deleted tasks
                printf "Enter the task name :\n"
                read task_name
                printf "Enter the date of deletion :\n"
                read date
                printf "Enter the time of deletion :\n"
                read time
                cat done.txt | grep "${task_name}"  | while read line
                    do
                    echo "$line       $date , $time">>deleted.txt
                    sed -i "/$task_name/ d" done.txt
                    printf "\tOperation done..\n"
                    done
                break
            ;;
            ${menu_array[5]})
                if [ ! -s ./deleted.txt ]; then
                    printf "\n\tNothing to display..\n"
                else     
                    cat deleted.txt
                    printf "\n\n"
                fi
                break
            ;;
            ${menu_array[6]})
            PS3="Choose an item : "
            select choice in "done" "undone" "deleted"
            do 
                case ${choice} in 
                "done")
                if [ ! -s ./done.txt ]; then
                    echo "\n\tNothing to display..\n"
                else
                printf "Enter the task name :\n"
                read task_name
                cat done.txt | grep ${task_name}  | while read line
                do
                echo $line
                done
                fi
                break
                ;;
                "undone")
                printf "Enter the task name :\n"
                read task_name
                cat undone.txt | grep ${task_name}  | while read line
                do
                echo $line
                done
                break
                ;;
                "deleted")
                printf "Enter the task name :\n"
                read task_name
                cat deleted.txt | grep "${task_name}"  | while read line
                do
                echo $line
                done
                break
                ;;
                esac
            done
            break
            ;;
            ${menu_array[7]})
            echo bye
            exit
            ;;
            *)
            echo "invalid input"
            ;;
            
        esac
        
    done
    
done