# Proxy Design Pattern

O proxy é um GoF estrutural cujo objetivo é encapsular um outro objeto. O proxy pode encapsular qualquer tipo de objeto ou recurso que seja custoso para o sistema ou impossível de se duplicar, ou seja, é um objeto que é acessado pelo cliente para acessar o objeto de real interesse por trás dos panos.

O proxy pode apenas passar os dados requisitados para frente, ou pode tambem adicionar alguma camada de lógica adicional. Funcionalidades extras podem ser adicionadas, como por exemplo adicionar resultados de operações custosas em cache ou fazer algum tipo de validação de dados antes de passar para o objeto real.

O uso do proxy para o cliente deve ser como usar o objeto real, pois ambos devem implementar a mesma interface.
