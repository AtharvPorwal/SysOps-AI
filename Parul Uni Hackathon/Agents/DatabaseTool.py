from pgvector.psycopg2 import register_vector
import psycopg2
from openai import OpenAI
client = OpenAI()

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input = [text], model=model).data[0].embedding

# text = "hii"
# print(len(get_embedding(text, model="text-embedding-3-small")))


conn = psycopg2.connect("dbname=ImgVec user=postgres password=root")
cur = conn.cursor()
register_vector(conn)


# cur.execute("CREATE TABLE WinPyCommands (id serial PRIMARY KEY, CommandDis text, CommandEmb vector(1536) )")
# conn.commit()

def AddCmds(CommandDis):
    print(CommandDis)
    CommandEmb = get_embedding(CommandDis, model="text-embedding-3-small")
    cur.execute("INSERT INTO WinPyCommands (CommandDis,CommandEmb) VALUES (%s, %s)", (CommandDis , CommandEmb))
    conn.commit()

def Retrive(Text):
    Output = []
    TextEmb = get_embedding(Text, model="text-embedding-3-small")

    string_representation = "["+ ",".join(str(x) for x in TextEmb) +"]"
    cur.execute("SELECT * FROM WinPyCommands ORDER BY CommandEmb <-> %s LIMIT 2;", (string_representation,))

    rows = cur.fetchall()
    OutputText = ""

    for row in rows:
        print(row[0],row[1])
        OutputText += row[1]
    return OutputText + "\n\n"

import json

def read_and_print_commands(json_file_path):
    """
    Reads a JSON file containing a list of command objects and prints their details.
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)  # Load the JSON data

        # Iterate over each command in the JSON file
        for index, item in enumerate(data, start=1):
            command = item.get("command", "N/A")
            description = item.get("description", "N/A")
            usage = item.get("usage", "N/A")
            details = item.get("details", "N/A")
            AddCmds(command+description+usage+details)


    except FileNotFoundError:
        print(f"Error: The file '{json_file_path}' was not found.")
    except json.JSONDecodeError:
        print("Error: Could not decode JSON. Please ensure the file is valid JSON.")

if __name__ == "__main__":
    read_and_print_commands("Tools\Data\cmdwi.json")
    Queary = input("Enter Query: ")
    print(Retrive(Queary))