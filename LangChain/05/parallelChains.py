from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()

llm1 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

llm2 = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3.5-397B-A17B"
)


model1 = ChatHuggingFace(llm=llm1)
model2 = ChatHuggingFace(llm=llm2)

prompt1 = PromptTemplate(
    template='Generate a short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate 5 short question and answers from the following text\n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}', 
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()


parallel_chain = RunnableParallel({
    'notes' : prompt1 | model2 | parser,
    'quiz' : prompt2 | model1 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = '''
**Support Vector Machine (SVM)** is a supervised machine learning algorithm used for both **classification and regression tasks**, though it is most commonly applied to classification problems. The main goal of SVM is to find the **best decision boundary (hyperplane)** that separates data points of different classes with the **maximum margin**.

In a classification problem, data points are represented as vectors in an n-dimensional feature space. SVM tries to find a hyperplane that divides the dataset into different classes. Among all possible hyperplanes, SVM selects the one that **maximizes the distance between the hyperplane and the nearest data points from each class**. This distance is called the **margin**, and maximizing it helps improve the model’s ability to generalize to unseen data.

The data points that lie closest to the decision boundary are known as **support vectors**. These points are critical because they directly influence the position and orientation of the hyperplane. If the support vectors change, the hyperplane also changes. All other points in the dataset do not significantly affect the boundary once it is determined.

In many real-world problems, the data may not be linearly separable in its original feature space. To handle such situations, SVM uses a technique called the **kernel trick**. The kernel trick maps the input data into a **higher-dimensional space** where it becomes easier to separate the classes using a linear hyperplane. Commonly used kernel functions include the **linear kernel, polynomial kernel, radial basis function (RBF) kernel, and sigmoid kernel**. The RBF kernel is particularly popular because it can model complex decision boundaries.

SVM also includes a **regularization parameter (C)** that controls the trade-off between maximizing the margin and minimizing classification errors. A small value of C allows a wider margin but may tolerate more misclassifications, while a large value of C tries to classify all training points correctly but may lead to overfitting.

One of the major advantages of SVM is its effectiveness in **high-dimensional spaces**, making it suitable for applications such as **text classification, image recognition, bioinformatics, and handwriting recognition**. Additionally, SVM tends to perform well even when the number of features is larger than the number of samples.

However, SVM can be computationally expensive for very large datasets and requires careful selection of kernel functions and hyperparameters. Despite these limitations, SVM remains a powerful and widely used algorithm in machine learning due to its strong theoretical foundation and robust performance.

'''
# result = chain.invoke({'text' : text})

chain.get_graph().print_ascii()

# print(result)