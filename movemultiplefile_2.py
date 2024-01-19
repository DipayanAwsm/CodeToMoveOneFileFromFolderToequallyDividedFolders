import os
import shutil
print("hi")
foldercapacity=100 # this how many files be in the folder
def move_files(source_folder, destination_folders):
    # Ensure source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return

    # Ensure destination folders exist, create if not
    for folder in destination_folders:
        os.makedirs(folder, exist_ok=True)

    # Iterate over files in the source folder
    count =0
    list_of_FileNames_inFolder =os.listdir(source_folder)
    NumberOfFiles = len(list_of_FileNames_inFolder)
    
    
    list_of_FileNames_inFolder =os.listdir(source_folder)  
    print("type:",type(list_of_FileNames_inFolder))
    i=0 
    print("NumberOfFiles:",NumberOfFiles)
    
    for destFolderName in destination_folders :            
        for j in range(foldercapacity):
            filename=list_of_FileNames_inFolder[i]
            print(filename)
            
            if not os.path.exists(filename):
                print(f"The file '{filename}' exists.")
                    
                        
                destination_path = destFolderName
                source_path = os.path.join(source_folder, filename)
                shutil.move(source_path, destination_path)
                print(f"Moved '{filename}' to '{destination_path}' folder.")
                list_of_FileNames_inFolder.remove(filename)
                #i=i+1
                print("i",i)
                print("now source size",len(list_of_FileNames_inFolder))
                  
        
        
    #######################################################
    
    

# Example usage:
source_folder = "D:/Photos/2023_11_14_mobile_backup"
destination_folders = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100","101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120","121","122","123","124","125","126","127","128","129","130","131","132","133","134","135","136","137","138","139","140","141","142","143"]
#destination_folders = ["11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100","101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120","121","122","123","124","125","126","127","128","129","130","131","132","133","134","135","136","137","138","139","140","141","142","143"]

move_files(source_folder, destination_folders)
