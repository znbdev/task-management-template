# 📌 [Java Task Name] Development Board

## 1. 📄 Basic Information

| Item          | Content                 |
|:------------|:-------------------|
| **Owner**   | @Fill in owner            |
| **Requester/Stakeholder** | Fill in requester              |
| **Start Date**    | YYYY-MM-DD         |
| **Due Date**      | YYYY-MM-DD         |
| **Priority**      | 🔴 P0-Urgent / 🟠 P1-High / 🟡 P2-Medium / 🔵 P3-Low |
| **Status**  | 🟩 Not Started / 🟨 In Progress / 🟦 Blocked / ⬜ Completed / ❌ Cancelled |
| **Task Type** | Feature Development / Bug Fix / Performance Optimization / Refactoring / API Development / Other |

---

## 2. 🎯 Technical Requirements & Deliverables

### Requirements Overview
> Briefly describe the technical problem to be solved or the business functionality to be implemented

### Technical Solution Highlights
*   **Core Tech Stack**: (e.g., Spring Boot 2.7 + MyBatis + MySQL 8.0)
*   **Design Patterns**: (e.g., Strategy Pattern, Factory Pattern, etc.)
*   **Key Dependencies**: (e.g., Need to introduce Redis cache, message queue, etc.)
*   **API Specifications**: (e.g., RESTful API, return unified Result wrapper)

### Key Deliverables
- [ ] Core business code (Service/Controller/DAO layers)
- [ ] Unit tests (coverage ≥ 80%)
- [ ] Integration test cases
- [ ] API documentation (Swagger/YApi)
- [ ] Database scripts (DDL/DML)
- [ ] Technical design document (if needed)
- [ ] Deployment configuration guide

### Acceptance Criteria
*   ✅ Functionality meets requirements and passes QA testing
*   ✅ Unit test coverage ≥ 80%, core logic 100% covered
*   ✅ API response time < X ms (P95)
*   ✅ No critical Code Review issues
*   ✅ Passes performance testing (if required)
*   ✅ Complete logging for troubleshooting

---

## 3. ⏳ Effort Estimation & Actual Tracking (WBS)

> *Note: Estimated effort (E) and actual effort (A) are in hours (h). Individual tasks should not exceed 4h.*

| Phase           | Task Breakdown            | Estimated Effort (E)  | Actual Effort (A)  | Progress/Notes         |
|:-------------|:---------------------------------|:---------:|:---------:|:--------------|
| **1. Research & Design** | 📝 Requirements analysis & existing code review                  |   0.0h    |   0.0h    |               |
|              | 🔍 Technical solution research (framework selection/middleware evaluation)          |   0.0h    |   0.0h    |               |
|              | 📐 Architecture design / Class diagram design / API definition            |   0.0h    |   0.0h    |               |
|              | 📋 Database design (table structure/indexes/SQL optimization)         |   0.0h    |   0.0h    |               |
|              | 👥 Technical solution review                       |   0.0h    |   0.0h    |               |
| **2. Environment Setup**  | 💻 Development environment setup (JDK/Maven/IDE configuration)     |   0.0h    |   0.0h    |               |
|              | 🗄 Database initialization / Migration script creation              |   0.0h    |   0.0h    |               |
|              | 🔧 Dependency introduction & configuration (pom.xml/application.yml) |   0.0h    |   0.0h    |               |
| **3. Core Development**  | 🛠 Controller layer development (API implementation)         |   0.0h    |   0.0h    |               |
|              | 🛠 Service layer development (business logic)             |   0.0h    |   0.0h    |               |
|              | 🛠 DAO/Mapper layer development (data access)          |   0.0h    |   0.0h    |               |
|              | 🛠 DTO/VO/Entity definition               |   0.0h    |   0.0h    |               |
|              | 🛠 Utility/support class development                     |   0.0h    |   0.0h    |               |
|              | 🔐 Access control & security validation                    |   0.0h    |   0.0h    |               |
|              | 📝 Logging & exception handling                    |   0.0h    |   0.0h    |               |
| **4. Testing & Optimization** | 🧪 Unit test writing (JUnit/Mockito)        |   0.0h    |   0.0h    |               |
|              | 🧪 Integration test writing (@SpringBootTest)    |   0.0h    |   0.0h    |               |
|              | 🐛 Local self-testing & debugging                       |   0.0h    |   0.0h    |               |
|              | ⚡ Performance optimization (SQL tuning/cache strategy/async processing)     |   0.0h    |   0.0h    |               |
| **5. Review & Revision** | 👥 Code Review             |   0.0h    |   0.0h    |               |
|              | 🔄 Code modification based on review feedback                   |   0.0h    |   0.0h    |               |
|              | 🔄 SonarQube quality check & fixes             |   0.0h    |   0.0h    |               |
| **6. Delivery & Deployment** | 📋 API documentation completion (Swagger annotations)         |   0.0h    |   0.0h    |               |
|              | 📋 Technical documentation (design document/user guide)          |   0.0h    |   0.0h    |               |
|              | 🧪 Test handover preparation & QA coordination                   |   0.0h    |   0.0h    |               |
|              | 🐛 Bug fixing & regression testing                  |   0.0h    |   0.0h    |               |
|              | 🚀 Deployment (CI/CD configuration/release verification)         |   0.0h    |   0.0h    |               |
| **📊 Total**     | **Total Effort**                      | **0.0h**  | **0.0h**  | **Variance: --%** |

---

## 4. 🏗️ Technical Architecture & Design

### Module Structure
```
com.example.project
├── controller      # Control layer (API entry point)
├── service         # Business logic layer
│   ├── impl       # Implementation classes
│   └── interface  # Interface definitions
├── mapper          # Data access layer (MyBatis)
├── entity          # Entity classes (corresponding to database tables)
├── dto             # Data Transfer Objects
├── vo              # View Objects
├── config          # Configuration classes
├── constant        # Constant definitions
├── exception       # Custom exceptions
├── util            # Utility classes
└── aspect          # AOP aspects (if needed)
```

### Key Technical Decisions
*   **Decision 1**: [Describe technology selection and reasons]
    *   Alternative solutions: XXX
    *   Selection rationale: XXX
*   **Decision 2**: [Describe design pattern application]
    *   Application scenario: XXX
    *   Advantage analysis: XXX

### Database Design
#### Table Structure Changes
```sql
-- Create/Modify table SQL
CREATE TABLE example_table (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    column_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_column_name (column_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

#### Index Optimization
*   Index 1: `idx_xxx` - For XXX query scenarios
*   Index 2: `idx_yyy` - For YYY sorting scenarios

### API Design
#### API List
| API Name | HTTP Method | Path | Description |
|:-------|:---------|:---|:---|
| API 1  | GET      | `/api/xxx` | Get XXX |
| API 2  | POST     | `/api/xxx` | Create XXX |
| API 3  | PUT      | `/api/xxx/{id}` | Update XXX |
| API 4  | DELETE   | `/api/xxx/{id}` | Delete XXX |

#### Request/Response Examples
```json
// Request example
{
  "fieldName": "value",
  "anotherField": 123
}

// Response example
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 1,
    "fieldName": "value"
  }
}
```

---

## 5. ⚠️ Risks, Dependencies & Buffer (Risk & Buffer)

### External Dependencies
*   **Team Dependencies**:
    *   Need frontend support for API integration
    *   Need DBA to review database design
    *   Need DevOps to configure server resources/domain
*   **Third-party Dependencies**:
    *   Waiting for XX service to provide API documentation
    *   Need to introduce XX middleware (Redis/MQ/ES, etc.)

### Technical Risks
*   **Performance Risk**: Large data volume queries may cause slow responses
    *   *Mitigation*: Perform SQL optimization in advance, consider pagination/cache/async processing
*   **Compatibility Risk**: New version may affect old functionality
    *   *Mitigation*: Conduct thorough regression testing, maintain backward-compatible APIs
*   **Concurrency Risk**: Data inconsistency may occur in high-concurrency scenarios
    *   *Mitigation*: Use distributed locks/optimistic locking/transaction isolation
*   **Security Risk**: SQL injection/XSS/unauthorized access
    *   *Mitigation*: Parameter validation, prepared statements, permission interceptors

### Project Risks
*   Requirements change risk: Mid-stream requirement adjustments causing rework
    *   *Mitigation*: Confirm requirement scope in advance, changes must go through review process
*   Schedule risk: Technical challenges take longer than expected
    *   *Mitigation*: Reserve buffer time, escalate risks promptly

### Buffer Mechanism
*   It's recommended to add **15% - 20%** risk buffer time to the total estimated effort
*   Current Buffer: **X.Xh** (X% of total effort)

---

## 6. 📝 Daily Follow-up & Notes (Daily Log)

### 📅 YYYY-MM-DD (Today's Plan)
- [ ] Complete XXX Service layer development
- [ ] Write XXX unit tests
- [ ] Integrate XXX API with frontend
*💡 Notes/Blockers:*
*Record technical challenges, temporary decisions, items needing coordination*

### 📅 YYYY-MM-DD (Yesterday's Review)
- [x] Complete XXX Controller layer development
- [x] Complete database table design and pass review
- [ ] XXX API development (Delay reason: Third-party API documentation delayed)

---

## 7. 🧪 Testing Checklist

### Unit Testing
- [ ] Service layer core business logic testing (coverage ≥ 80%)
- [ ] Boundary condition testing (null values/abnormal values/extreme values)
- [ ] Exception handling testing

### Integration Testing
- [ ] Database CRUD operation testing
- [ ] Complete API flow testing
- [ ] Transaction consistency testing

### Performance Testing (if needed)
- [ ] Single API load testing (target QPS: XXX)
- [ ] Database slow query detection
- [ ] Memory leak detection

### Security Testing
- [ ] SQL injection testing
- [ ] XSS attack testing
- [ ] Permission validation testing
- [ ] Sensitive data encryption verification

---

## 8. 📋 Code Review Checklist

### Code Standards
- [ ] Follow Alibaba Java Development Manual
- [ ] Naming conventions (class/method/variable names are meaningful)
- [ ] Consistent code formatting (use IDE formatter)
- [ ] Extract magic numbers/strings to constants

### Design Quality
- [ ] Single Responsibility Principle (clear class/method responsibilities)
- [ ] Avoid deep nesting (≤ 3 levels)
- [ ] Avoid overly long methods (≤ 80 lines)
- [ ] Appropriate use of design patterns

### Performance Optimization
- [ ] Avoid N+1 query problems
- [ ] Appropriate use of caching
- [ ] Avoid large object creation
- [ ] Timely resource release (IO/connection pools)

### Exception Handling
- [ ] Don't swallow exceptions (must log or throw)
- [ ] Use specific exception types
- [ ] Correct transaction rollback configuration

### Logging Standards
- [ ] Key business points have logging
- [ ] Use correct log levels (ERROR/WARN/INFO/DEBUG)
- [ ] Don't print sensitive information (passwords/ID numbers, etc.)
- [ ] Logs contain sufficient context information

### Security
- [ ] Complete parameter validation (@Valid/@NotNull, etc.)
- [ ] SQL uses prepared statements (prevent injection)
- [ ] Proper permission validation
- [ ] Sensitive data encrypted at rest

---

## 9. 🚀 Deployment & Operations

### Deployment Checklist
- [ ] Environment-specific configuration files (dev/test/prod)
- [ ] Database scripts ready (table creation/initial data/rollback scripts)
- [ ] Dependent services confirmed (Redis/MQ/ES, etc. ready)
- [ ] CI/CD pipeline configured
- [ ] Health check endpoint working (/actuator/health)

### Monitoring & Alerting
*   **Key Metrics**:
    *   API response time (P95 < X ms)
    *   Error rate (< X%)
    *   JVM memory usage (< 80%)
    *   GC frequency and duration
*   **Log Collection**: ELK/Splunk configured
*   **Distributed Tracing**: SkyWalking/Zipkin integrated (if needed)

### Rollback Plan
*   **Code Rollback**: Git revert to previous version tag
*   **Database Rollback**: Prepare rollback SQL scripts
*   **Verification Steps**: Verify core functionality works after rollback

---

## 10. 📚 Related Resources & References

*   📎 Requirements document: [Link]
*   📎 Technical design document: [Link]
*   📎 API documentation: [Swagger/YApi link]
*   📎 Database ER diagram: [Link]
*   📎 Related Issue: [#Number]
*   📎 References:
    *   Spring official documentation
    *   MyBatis user guide
    *   Alibaba Java Development Manual

---

## 11. 🔄 Change History

| Date         | Change Description          | Changed By   |
|:-----------|:----------------|:------|
| YYYY-MM-DD | Initial creation          | @Owner  |
|            | Technical solution adjustment        |       |
|            | Added XXX feature requirement   |       |

---

## 💡 Java Development Best Practices

### Layered Architecture Standards
*   **Controller Layer**: Only handles parameter reception, validation, response wrapping; no business logic
*   **Service Layer**: Core business logic, transaction control, calls Mapper and other Services
*   **Mapper Layer**: Only handles database CRUD; complex SQL written in XML
*   **No Cross-layer Calls**: Controller → Service → Mapper, cannot skip layers

### Common Pitfalls & Avoidance
*   ❌ **NullPointerException**: All external inputs must be null-checked; use Optional/Objects.requireNonNull
*   ❌ **Transaction Failure**: @Transactional only works on public methods; same-class calls don't go through proxy
*   ❌ **Loop Queries**: Replace loop single queries with batch queries; use IN clause or JOIN
*   ❌ **Large Transactions**: Keep transaction scope minimal; avoid calling remote APIs within transactions
*   ❌ **Hardcoding**: Write configuration items in application.yml; define constants centrally

### Performance Optimization Techniques
*   ✅ **Database**: Proper indexing, avoid SELECT *, paginated queries, read-write separation
*   ✅ **Caching**: Redis cache for hot data; watch for cache penetration/avalanche/breakdown
*   ✅ **Async**: Async processing for non-core flows (@Async/message queue)
*   ✅ **Connection Pool**: Properly configure HikariCP parameters (max connections/timeout)

### Debugging Techniques
*   Use IDEA Debug mode for breakpoint debugging
*   Focus on ERROR/WARN levels when reviewing logs
*   Use Arthas for online production issue diagnosis (use cautiously)
*   Use Postman/Apifox for API testing

### Recommended Toolchain
*   **Build Tools**: Maven / Gradle
*   **Code Quality**: SonarQube / Checkstyle
*   **API Documentation**: Swagger / Knife4j / YApi
*   **Testing Framework**: JUnit 5 + Mockito
*   **Logging Framework**: SLF4J + Logback
*   **JSON Processing**: Jackson / Fastjson2
*   **Utility Libraries**: Lombok / Hutool / Apache Commons
