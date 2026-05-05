<template>
  <div class="app">
    <h1>📝 My Todo App</h1>
    <p class="subtitle">Built with Vue + FastAPI + Docker 🐳</p>

    <!-- Add Todo -->
    <div class="add-todo">
      <input
        v-model="newTodo"
        @keyup.enter="addTodo"
        placeholder="Add a new todo..."
      />
      <button @click="addTodo">Add</button>
    </div>

    <!-- Loading -->
    <p v-if="loading">Loading todos... ⏳</p>

    <!-- Todo List -->
    <div class="todo-list">
      <div
        v-for="todo in todos"
        :key="todo.id"
        class="todo-item"
        :class="{ done: todo.done }"
      >
        <span>{{ todo.done ? '✅' : '⏳' }}</span>
        <span>{{ todo.title }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      todos: [],
      newTodo: '',
      loading: false,
    }
  },
  async mounted() {
    await this.fetchTodos()
  },
  methods: {
    async fetchTodos() {
      this.loading = true
      const res = await fetch('http://localhost:8000/todos')
      this.todos = await res.json()
      this.loading = false
    },
    async addTodo() {
      if (!this.newTodo.trim()) return
      await fetch('http://localhost:8000/todos', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: this.newTodo })
      })
      this.newTodo = ''
      await this.fetchTodos()
    }
  }
}
</script>

<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: system-ui, sans-serif;
  background: #0d1117;
  color: #e6edf3;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  padding: 40px 20px;
}
.app {
  width: 100%;
  max-width: 500px;
}
h1 {
  font-size: 28px;
  margin-bottom: 8px;
  color: #58a6ff;
}
.subtitle {
  color: #8b949e;
  margin-bottom: 28px;
  font-size: 14px;
}
.add-todo {
  display: flex;
  gap: 10px;
  margin-bottom: 24px;
}
input {
  flex: 1;
  padding: 12px 16px;
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 8px;
  color: #e6edf3;
  font-size: 15px;
}
input:focus {
  outline: none;
  border-color: #58a6ff;
}
button {
  padding: 12px 20px;
  background: #58a6ff;
  color: #000;
  border: none;
  border-radius: 8px;
  font-weight: 700;
  cursor: pointer;
  font-size: 15px;
}
button:hover { background: #79c0ff; }
.todo-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 16px;
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 8px;
  margin-bottom: 10px;
  font-size: 15px;
}
.todo-item.done {
  opacity: 0.5;
  text-decoration: line-through;
}
</style>