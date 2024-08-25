def save_to_file(file_name, jobs): 
    file = open(f"{file_name}.csv", "w")
    file.write("제목,회사,link")

    for job in jobs: 
        print(job)
        file.write(
            f"{job['title']},{job['company']},{job['link']}\n"
        )
    file.close()